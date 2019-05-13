*** Settings ***
Library                       RobotProcessLibrary

*** Keywords ***

Fogyasztasok beirasa
    [Arguments]                 ${gaz}  ${villany}  ${viz}  ${kozoskoltseg}

    ${empty_cell}=              Get First Empty Cell Below  B4
    Set Cell Value              ${empty_cell}  ${gaz}
    ${empty_cell}=              Get Cell Right To  ${empty_cell}
    Set Cell Value              ${empty_cell}  ${villany}
    ${empty_cell}=              Get Cell Right To  ${empty_cell}
    Set Cell Value              ${empty_cell}  ${viz}
    ${empty_cell}=              Get Cell Right To  ${empty_cell}
    Set Cell Value              ${empty_cell}  ${kozoskoltseg}

Gaz kiadasok
    [Arguments]                 ${fogyasztas}
    ${gaz_ar}=                  Get Cell Value  B4
    ${ures_B}=                  Get First Empty Cell Below  B7
    ${gaz_osszeg}=              Evaluate  ${fogyasztas}*${gaz_ar}
    Set Cell Value              ${ures_B}  ${gaz_osszeg}

Villany kiadasok
    [Arguments]                 ${fogyasztas}
    ${villany_ar}=              Get Cell Value  B5
    ${ures_C}=                  Get First Empty Cell Below  C7
    ${villany_osszeg}=          Evaluate  ${fogyasztas}*${villany_ar}
    Set Cell Value              ${ures_C}  ${villany_osszeg}

Viz kiadasok
    [Arguments]                 ${fogyasztas}
    ${viz_ar}=                  Get Cell Value  B6
    ${ures_D}=                  Get First Empty Cell Below  D7
    ${viz_osszeg}=              Evaluate  ${fogyasztas}*${viz_ar}
    Set Cell Value              ${ures_D}  ${viz_osszeg}

Kozos koltseg kiadasok
    [Arguments]                 ${fizetes}
    ${kozos_ar}=                Get Cell Value  B3
    ${ures_E}=                  Get First Empty Cell Below  E8
    Run Keyword If  "${fizetes}"=="fizetve"
        ...  Set Cell Value  ${ures_E}  ${kozos_ar}

Osszes kiadas
    ${ures_F}=                  Get First Empty Cell Below  F8
    ${mezo_E}=                  Get Cell Left To  ${ures_F}
    ${ures_B}=                  Get First Empty Cell Below  B7
    ${mezo_B}=                  Get Cell Above  ${ures_B}
    Add Formula To Cell         ${ures_F}  =SUM(${mezo_B}:${mezo_E})
    Set Cell Style              ${ures_F}  bold

*** Processes ***
rezsi kiadasok
    [Tags]                      rezsi

    ${fogyasztas}=              Ocr Image   fogy.png
    ${gaz}=                     Evaluate  re.search('gaz:(.*)m3', "${fogyasztas}").group(1).strip()  modules=re
    ${villany}=                 Evaluate  re.search('vill:(.*)kwh', "${fogyasztas}").group(1).strip()  modules=re
    ${viz}=                     Evaluate  re.search('viz:(.[^(m3)]*)m3', "${fogyasztas}").group(1).strip()  modules=re
    ${kozoskoltseg}=            Evaluate  re.search('kk:(.*)', "${fogyasztas}").group(1).strip()  modules=re


    Open Workbook               rezsi.xlsx
    Set Active Worksheet        fogyasztás

    Fogyasztasok beirasa        ${gaz}  ${villany}  ${viz}  ${kozoskoltseg}

    Set Active Worksheet        kiadások

    Gaz kiadasok                ${gaz}
    Villany kiadasok            ${villany}
    Viz kiadasok                ${viz}
    Kozos koltseg kiadasok      ${kozoskoltseg}

    Osszes kiadas




