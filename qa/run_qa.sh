#!/usr/bin/env sh
set -eu

ROOT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
TOOL_IMAGE="${EVORAO_TOOL_IMAGE:-evoratools/schemasheets:0.4.0_stable}"
PYSHACL_IMAGE="${EVORAO_PYSHACL_IMAGE:-python:3.12-alpine}"
ROBOT_IMAGE="${EVORAO_ROBOT_IMAGE:-obolibrary/robot:latest}"
REASONER="${EVORAO_REASONER:-ELK}"
STRICT_REASONER="${EVORAO_STRICT_REASONER:-JFact}"

REPORT_DIR="$ROOT_DIR/qa/reports"
mkdir -p "$REPORT_DIR"

echo "EVORAO QA starting"
echo "Repository: $ROOT_DIR"
echo "Reports: $REPORT_DIR"

run_tool_python() {
  docker run --rm \
    --user root \
    -v "$ROOT_DIR:/workdir" \
    -w /workdir \
    "$TOOL_IMAGE" \
    python3 "$@"
}

run_tool_python qa/scripts/qa_checks.py structural
run_tool_python qa/scripts/qa_checks.py competency

echo "Running SHACL fixture validation"
docker run --rm \
  --user root \
  -v "$ROOT_DIR:/workdir" \
  -w /workdir \
  "$PYSHACL_IMAGE" \
  sh -lc "pip install --quiet pyshacl==0.30.1 >/tmp/pyshacl-install.log && \
    pyshacl -s models/subsidiary_models/shacl/evora_schema.shacl.ttl -f human qa/fixtures/valid_catalogue.ttl > qa/reports/shacl-valid.txt && \
    pyshacl -s models/subsidiary_models/shacl/evora_schema.shacl.ttl -f turtle qa/fixtures/valid_catalogue.ttl > qa/reports/shacl-valid.ttl && \
    if pyshacl -s models/subsidiary_models/shacl/evora_schema.shacl.ttl -f human qa/fixtures/invalid_missing_required_metadata.ttl > qa/reports/shacl-invalid.txt; then exit 14; fi && \
    pyshacl -s models/subsidiary_models/shacl/evora_schema.shacl.ttl -f turtle qa/fixtures/invalid_missing_required_metadata.ttl > qa/reports/shacl-invalid.ttl || true"

run_tool_python qa/scripts/qa_checks.py shacl-summary

echo "Running blocking OWL reasoning with ROBOT/$REASONER"
if docker run --rm \
  -v "$ROOT_DIR:/workdir" \
  -w /workdir \
  "$ROBOT_IMAGE" \
  robot reason --reasoner "$REASONER" --input models/owl/evora_ontology.owl.ttl --output /tmp/evorao-reasoned.owl > "$REPORT_DIR/reasoning.txt" 2>&1; then
  printf '{"status":"pass","reasoner":"%s","tool":"ROBOT"}\n' "$REASONER" > "$REPORT_DIR/reasoning.json"
else
  printf '{"status":"fail","reasoner":"%s","tool":"ROBOT","report":"qa/reports/reasoning.txt"}\n' "$REASONER" > "$REPORT_DIR/reasoning.json"
  echo "ROBOT/$REASONER reasoning failed; see qa/reports/reasoning.txt"
  exit 15
fi

echo "Running blocking OWL reasoning over ontology plus valid fixture with ROBOT/$REASONER"
if docker run --rm \
  -v "$ROOT_DIR:/workdir" \
  -w /workdir \
  "$ROBOT_IMAGE" \
  robot merge --input models/owl/evora_ontology.owl.ttl --input qa/fixtures/valid_catalogue.ttl \
    reason --reasoner "$REASONER" --output /tmp/evorao-fixture-reasoned.owl > "$REPORT_DIR/reasoning-fixture.txt" 2>&1; then
  printf '{"status":"pass","reasoner":"%s","tool":"ROBOT","fixture":"qa/fixtures/valid_catalogue.ttl"}\n' "$REASONER" > "$REPORT_DIR/reasoning-fixture.json"
else
  printf '{"status":"fail","reasoner":"%s","tool":"ROBOT","fixture":"qa/fixtures/valid_catalogue.ttl","report":"qa/reports/reasoning-fixture.txt"}\n' "$REASONER" > "$REPORT_DIR/reasoning-fixture.json"
  echo "ROBOT/$REASONER reasoning with the valid fixture failed; see qa/reports/reasoning-fixture.txt"
  exit 16
fi

# The strict DL reasoner is informative rather than blocking. Its report keeps
# OWL DL profile or datatype issues visible without replacing the ELK gate.
echo "Recording non-blocking ROBOT/$STRICT_REASONER DL check"
if docker run --rm \
  -v "$ROOT_DIR:/workdir" \
  -w /workdir \
  "$ROBOT_IMAGE" \
  robot reason --reasoner "$STRICT_REASONER" --input models/owl/evora_ontology.owl.ttl --output /tmp/evorao-strict-reasoned.owl > "$REPORT_DIR/reasoning-strict.txt" 2>&1; then
  printf '{"status":"pass","reasoner":"%s","tool":"ROBOT"}\n' "$STRICT_REASONER" > "$REPORT_DIR/reasoning-strict.json"
else
  docker run --rm \
    --user root \
    -v "$ROOT_DIR:/workdir" \
    -w /workdir \
    "$ROBOT_IMAGE" \
    robot explain --mode inconsistency --reasoner "$STRICT_REASONER" --input models/owl/evora_ontology.owl.ttl --explanation qa/reports/reasoning-strict-explanation.md --max 3 >> "$REPORT_DIR/reasoning-strict.txt" 2>&1 || true
  printf '{"status":"warn","reasoner":"%s","tool":"ROBOT","report":"qa/reports/reasoning-strict.txt","explanation":"qa/reports/reasoning-strict-explanation.md"}\n' "$STRICT_REASONER" > "$REPORT_DIR/reasoning-strict.json"
fi

run_tool_python qa/scripts/qa_checks.py final-summary
echo "EVORAO QA passed"
