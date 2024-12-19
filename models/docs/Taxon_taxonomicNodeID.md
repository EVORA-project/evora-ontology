
# Slot: taxonomicNodeID

The taxonomic_Node Identifier as an identifier specific the current taxon in the corresponding release/version of the taxonomy

URI: [EVORA:Taxon_taxonomicNodeID](https://evora-project.eu/Taxon_taxonomicNodeID)


## Domain and Range

[Taxon](Taxon.md) &#8594;  <sub>0..1</sub> [String](types/String.md)

## Parents

 *  is_a: [taxonomicNodeID](taxonomicNodeID.md)

## Children


## Used by

 * [Taxon](Taxon.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | taxonomic node ID |
| **Comments:** | | NCBI does not have a taxon_node id, only a taxonomicID. Taxon_node id is Unique  in NCBI= Key of the taxon node !! Could be replaced by a composite key made of "taxonomic ID" + "has version" But can be referenced as it seems the "taxonomic node_ID" will be generated and provided by the ICTV |
| **Close Mappings:** | | dwc:taxonID |