## Codes
Currently, PicnicHealth uses the following standard code systems for each encounter and encounter items:

* <a target="_blank" href="http://loinc.org/">LOINC</a> for [Observation](#observations) and [LabTestResult](#lab-test-results) objects
* <a target="_blank" href="https://www.nlm.nih.gov/research/umls/rxnorm">RxNorm</a> for [MedicationStatement](#medication-statements) objects
* <a target="_blank" href="http://www.cdc.gov/nchs/icd/icd9cm.htm">ICD9-CM</a> for [Problem](#problems) objects

There are some cases where a codeable encounter or encounter items cannot be associated with any code in the above standard code systems. For those cases, we use a PicnicHealth built-in code system `Buffet` as an extension of the associated code. This `Buffet` code is a temporary code and is replaced by the standard code as an equivalent code is added to the standard code system. This allows any codes to be easily managable and reuseable.
