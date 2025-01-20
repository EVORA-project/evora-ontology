/**
 * Retrieves the current version and outputs it as plain text.
 */
function showCurrentVersion() {
  const version = getSpreadsheetVersion();
  const output = ContentService.createTextOutput(version);
  output.setMimeType(ContentService.MimeType.TEXT);
  return output;
}
