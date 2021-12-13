# Permit Data Standards

List of [committee membership](https://github.com/AAVLD-USAHA-ITStandards/Permit/blob/main/Governance/participants.md)

A few words on the documentation approach: 
 
First and foremost, the XML schema *is* the standard.  All other material is supplemental documentation, committee governance, etc.  The committee sometimes provides "bridge" schemas that will validate content in either of two versions to help implementers synchronize upgrading.

The documentation in human-readable format is a best effort at converting the structure and documentation elements in the schema.  It is for reference only.  If the documentation differs from the schema structure, the structure rules.  

The **Issues** section of this project contains open issues before the committee.  Some of these are being actively worked, while others are on-hold for a future major release, etc.  Anyone who sees problems or areas to improve the standard is encouraged to create a new Issue.  

The **Releases** section of this project contains the numbered release commits.  Releases are numbered Major.Minor.Editorial.  Implementers should be able to ignore differences between versions that vary only in the third part. Each release contains a zip and tar.gz file that contains the corresponding ecvi2.xsd file.

The **master** branch contains the current release *plus* any pending changes that have been approved by the committee and are awaiting release.

The **pending changes** branch contains the current release *plus* any pending changes both approved and currently under consideration. Each commit should corresponde as much as possible to one proposed solution to one issue.  

