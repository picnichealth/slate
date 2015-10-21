#!/usr/bin/python

import sys

files = [
  './source/resources/_medical_facility.md',
  './source/resources/_medical_practitioner.md',
  './source/resources/_patient.md',
  './source/resources/_lab_test_result.md',
  './source/resources/encounters/_encounter.md',
  './source/resources/encounter_items/_encounter_item.md',
  './source/resources/encounter_items/_note.md',
  './source/resources/encounter_items/_medication_statement.md',
  './source/resources/encounter_items/_observation.md',
  './source/resources/encounter_items/_condition.md',
  './source/resources/_code.md'
];

outFilePath = './source/includes/_resources.md'
beginPrivateTag = '<!--- begin private -->'
endPrivateTag = '<!--- end private -->'
mode = 'private' if 'private' in str(sys.argv) else 'public'

print "Preprocessing started for " + mode + "..."
with open(outFilePath, 'w') as outFile:
  for file in files:
    with open(file, 'r') as inFile:
      print "processing " + file
      skip = False
      for line in inFile:
        if beginPrivateTag in line:
          skip = True if mode == 'public' else False
        elif endPrivateTag in line:
          skip = False
        elif skip == False:
          outFile.write(line)
print "done!"
