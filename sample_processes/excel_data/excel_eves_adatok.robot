*** Settings ***
Library                    RobotProcessLibrary

*** Variables ***
${cell}=             A1
${sum}=              0
${max}=              0


*** Test Cases ***
Excel Sum Years
    Open Workbook       workspace/data.xlsx
    Set Active Worksheet  data

    :FOR    ${i}    IN RANGE    999999
    \  ${first_empty}=       Get First Empty Cell Below  ${cell}
    \  ${first_cell}=       Get Cell Below  ${cell}
    \  ${last_cell}=       Get Cell Above  ${first_empty}
    \  ${year}=       Get Cell Value  ${cell}
    \  Add Formula To Cell  ${first_empty}  =SUM(${first_cell}:${last_cell})  
    \  ${value}=         Get Cell Value  ${first_empty}
    \  ${sum}=            Evaluate  ${sum}+${value}
    \  Run Keyword If  ${value}>${max}  Run Keywords
           ...  Set Global Variable  ${max}  ${value}
           ...  AND  Set Global Variable  ${max_year}  ${year}
    \  Set Cell Background     ${first_empty}  GREEN
    \  ${cell}=        Get Cell Right To  ${cell}
    \  ${cell_value}=   Get Cell Value  ${cell}
    \  Exit For Loop If    ${cell_value} == None

    Create Worksheet  results
    Set Active Worksheet  results

    Set Cell Value  A1  sum:
    Set Cell Style  A1  bold
    Set Cell Value  A2  maximum:
    Set Cell Style  A2  bold
    Set Cell Value  A3  max year:
    Set Cell Style  A3  bold

    Set Cell Value  B1  ${sum}
    Set Font Size   B1  14
    Set Cell Value  B2  ${max}
    Set Font Size   B2  14
    Set Cell Value  B3  ${max_year}
    Set Font Size   B3  14

    Close Workbook