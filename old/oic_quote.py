from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import unittest
import time
import re


def setUp():
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.maximize_window()
    urls=["http://localhost:5612/login.max?preprocess=true#","http://www.maxprocessing.com:5612/login.max?preprocess=true"]
    driver.get(urls[1])
    print('The opened system is : %s' % driver.title)
    return driver


def login(driver):
    if check_timeout(driver, 'UserName', By.NAME) == 1:
        driver.find_element_by_name("UserName").send_keys("mwan")
        driver.find_element_by_name("password").send_keys("mark@123")
        driver.find_element_by_name("submit").click()


def test_ho3(driver):
    time.sleep(1)
    if check_timeout(driver, 'Application', By.LINK_TEXT) == 1:
        a_Application = driver.find_element_by_link_text('Application')
        a_Application.click()

        datas1 = {'Agency': 'Olympus Insurance Managers Inc - OI-10000',
                  'LOBType': 'Regular',
                  'LOB': 'Homeowners',
                  'FormType': 'HO-3',
                  'Usage': 'Primary',
                  'Occupancy': 'Owner',
                  'NewPurchase': 'No',
                  'Ownedby': '4',  # 1:Indivnameual, 2: Trust, 3: LLC, 4: Other
                  'FirstName': 'Test_auto2',
                  'LastName': 'Test_auto',
                  'DOB': time.strftime("%m/%d/%Y", time.localtime(time.time())),
                  'CompanyName': 'Case for auto test',
                  'ContactMethod': '1',  # 1:Phone, 2: Text/SMS, 3: E-mail
                  'CellPhone': '1234567',
                  'Email': 'Test_auto@126.com',
                  'SecondIns': '0',  # 0: N/A, 1: And
                  'Address1': '100 Magnolia Way',
                  'City': 'Bradenton',
                  'State': 'FL',
                  'Zip': '34209-7126',
                  #'County':'Manatee',
                  'BurglarAlarm': 'None',
                  'FireAlarm': 'None',
                  'AutomaticSprinklers': 'None',  # AutomaticSprinklers(HO) / SecuredCommunity(DF)
                  'Sprinkler': 'None'  # Only for DF
                  }

        datas2 = {'LOB': '2',
                  'FRM': '12',
                  'ProtectionClass': '04',
                  'Department': 'WEST MANATEE FS 2',
                  'FireHydrant': 'Within 1,000 feet',
                  'FireStation': 'Greater than 3 to 4 miles',
                  'YearofConstruction': '2016',
                  'YearofRoofInstallation': '2016',
                  'ConstructionClass': 'Frame',
                  'RoofGeometry': 'Hip Roof',
                  'DwellingType': 'Rowhouse',
                  'RoofMaterialType': 'Composition',
                  'NumberofUnits': '1',
                  'PermittedSubdivision': 'No',  # if PermittedSubdivision
                  'NumberofStories': '1',
                  'NumberofFamilies': '1',
                  'SquareFootage': '1000',
                  'NumberofBoarders': '0',
                  'FloodZone': 'AE',
                  'Territory': '582',
                  'DistanceToCoast': '2 miles to less than 3 miles',
                  'BCEG': '99',
                  'TierGroup': '0',
                  'PrimaryHeatSource': 'Central Electric Heat',
                  'TansksOnPremises': 'No'
                  }

        datas3 = {'LOB': '2',
                  'FRM': '12',
                  'CurrentAddressYears': '0',
                  'MailingAddrSameAsProperty': 'Yes',
                  'IsNewPurch': 'No',
                  'CurrentCarrier': 'Test_auto',
                  'ExpirationDateForCurrentPolicy': time.strftime("%m/%d/%Y", time.localtime(time.time())),
                  'YearsWithCurrentCarrier': '1',
                  'YearofRoofInstallation': '2016',
                  'PropertyInFloodZone': '1',
                  'HasFloodIns': 'No',
                  'Flood_CurrentCarrier': 'Test_auto',
                  'Flood_ExpirationDateForCurrentPolicy': time.strftime("%m/%d/%Y", time.localtime(time.time())),
                  'Flood_YearsWithCurrentCarrier': '1'
                  }

        datas4 = {'LOB': '2',
                  'FRM': '12',
                  'A': '$250000',
                  'B': '$0',
                  'C': '$125000',
                  'D': '$25000',
                  'E': '$100,000',
                  'F': '$1,000',
                  'HurricaneDeductible': '2%',
                  'AllOtherPerilsDeductible': '1%'
                  }

        opt_coverages = ('Increased Ordinance or Law', '')
        datas5 = {'LOB': '2',
                  'FRM': '12',
                  'OptCoverage': opt_coverages
                  }
        datas6 = {'LOB': '2',
                  'FRM': '12',
                  'UWQuestion_result': 'No'
                  }

        datas7 = {'LOB': '2',
                  'FRM': '12'
                  }

        datas8 = {'LOB': '2',
                  'FRM': '12',
                  'Premium': '$1,381.00',
                  'Fee': '$25.00',
                  'Surcharge': '$2.00',
                  'Total_Premium': '$1,408.00'
                  }

        if application_page1(driver, **datas1) == 1:
            if application_page2(driver, **datas2) == 1:
                if application_page3(driver, **datas3) == 1:
                    if application_page4(driver, **datas4) == 1:
                        if application_page5(driver, **datas5) == 1:
                            if application_page6(driver, **datas6) == 1:
                                if application_page7(driver, **datas7) == 1:
                                    application_page8(driver, **datas8)


def application_page1(driver, **kwargs):
    if check_timeout(driver, 'PQ_Agency', By.NAME) == 1:
        print('Enter into the application_page1 ---')
        Select(driver.find_element_by_name("PQ_Agency")).select_by_visible_text(kwargs['Agency'])

        if kwargs['LOBType'] == 'Takeout':
            lob_type = Select(driver.find_element_by_name("LOBType"))
            lob_type.select_by_visible_text(kwargs['LOBType'])
            driver.execute_script("$('#LOBType').change()")

        driver.implicitly_wait(5)
        lob_list = driver.find_elements_by_name('sLOB_Type')
        if kwargs['LOB'] == 'Homeowners':
            lob_list[0].click()
        else:
            lob_list[1].click()
            if check_timeout(driver, 'sDC_Code_Occupancy', By.NAME) == 1:
                Select(driver.find_element_by_name("sDC_Code_Occupancy")).select_by_visible_text(kwargs['Occupancy'])

        Select(driver.find_element_by_name("sFRM_ID")).select_by_visible_text(kwargs['FormType'])

        Select(driver.find_element_by_name("sDC_Code_Loc_Usage")).select_by_visible_text(kwargs['Usage'])
        driver.execute_script("$('#sDC_Code_Loc_Usage').change()")

        newPurcharse_list = driver.find_elements_by_name('PQLI_IsNewPurch')
        if kwargs['NewPurchase'] == 'Yes':
            newPurcharse_list[0].click()
        else:
            newPurcharse_list[1].click()

        ownedby_list = driver.find_elements_by_name("PQ_PropertyOwnedBy")
        if kwargs['Ownedby'] == '1':
            ownedby_list[2].click()
        elif kwargs['Ownedby'] == '2':
            ownedby_list[0].click()
            driver.find_element_by_name("PQ_CompanyName_Trust").send_keys(kwargs['CompanyName'])
        elif kwargs['Ownedby'] == '3':
            ownedby_list[1].click()
            driver.find_element_by_name("PQ_CompanyName_LLC").send_keys(kwargs['CompanyName'])
        else:
            ownedby_list[3].click()

        driver.implicitly_wait(1)
        driver.find_element_by_name("PQ_FirstName").send_keys(kwargs['FirstName'])
        driver.find_element_by_name("PQ_LastName").send_keys(kwargs['LastName'])
        driver.find_element_by_name("PQ_DOB").send_keys(kwargs['DOB'])

        contactmethod_list = driver.find_elements_by_name("PQ_ContactMethod")
        contactmethod_list[int(kwargs['ContactMethod']) - 1].click()

        driver.find_element_by_name("PQ_CellPhone").send_keys(kwargs['CellPhone'])
        driver.find_element_by_name("PQ_Email").send_keys(kwargs['Email'])

        secondins_list = driver.find_elements_by_name("PQ_SecondIns")
        if int(kwargs['SecondIns']) == 0:
            secondins_list[1].click()
        else:
            secondins_list[0].click()

        driver.find_element_by_name("PQ_Address1").send_keys(kwargs['Address1'])
        driver.find_element_by_name("PQ_City").send_keys(kwargs['City'])
        driver.find_element_by_name("PQ_State").send_keys(kwargs['State'])
        driver.find_element_by_name("PQ_Zip").send_keys(kwargs['Zip'])
        # time.sleep(1)
        if check_timeout(driver, 'address.suggestion', By.CSS_SELECTOR) == 1:
            driver.find_element_by_css_selector("address.suggestion").click()
            if check_timeout(driver, 'popup_ok', By.ID) == 1:
                driver.find_element_by_id("popup_ok").click()
                # driver.find_element_by_name("PQ_County").send_keys(kwargs['County'])

                Select(driver.find_element_by_name("BurglarAlarm")).select_by_visible_text(kwargs['BurglarAlarm'])
                Select(driver.find_element_by_name("FireAlarm")).select_by_visible_text(kwargs['FireAlarm'])

                if kwargs['LOB'] == 'Homeowners':
                    Select(driver.find_element_by_name("AutomaticSprinklers")).select_by_visible_text(kwargs['AutomaticSprinklers'])
                else:
                    Select(driver.find_element_by_name("SecuredCommunity")).select_by_visible_text(kwargs['AutomaticSprinklers'])
                    Select(driver.find_element_by_name("Sprinkler")).select_by_visible_text(kwargs['Sprinkler'])

                driver.find_element_by_name('Continue').click()
                if check_timeout(driver, 'DupeSubmitPage', By.NAME) == 1:
                    driver.find_element_by_name('DupeSubmitPage').click()
                    print('---  Leave the application_page1')
                    return 1
                else:
                    return 0
    else:
        return 0


def application_page2(driver, **kwargs):
    if check_timeout(driver, 'sDC_Code_Prot_Class', By.NAME) == 1:
        print('Enter into the application_page2 ---')
        Select(driver.find_element_by_name("sDC_Code_Prot_Class")).select_by_visible_text(kwargs['ProtectionClass'])
        driver.execute_script("$('#sDC_Code_Prot_Class').change()")
        Select(driver.find_element_by_name("PQLI_DistFromHydrant")).select_by_visible_text(kwargs['FireHydrant'])
        Select(driver.find_element_by_name("PQLI_DistFromFireStation")).select_by_visible_text(kwargs['FireStation'])
        driver.find_element_by_name("PQLI_FireDistrict").clear()
        driver.find_element_by_name("PQLI_FireDistrict").send_keys(kwargs['Department'])

        driver.find_element_by_name("PQLI_YrBuilt").clear()
        driver.find_element_by_name("PQLI_YrBuilt").send_keys(kwargs['YearofConstruction'])
        driver.find_element_by_name("PQLI_YrRoofInstall").clear()
        driver.find_element_by_name("PQLI_YrRoofInstall").send_keys(kwargs['YearofRoofInstallation'])

        Select(driver.find_element_by_name("sDC_Code_Const_Class")).select_by_visible_text(kwargs['ConstructionClass'])
        Select(driver.find_element_by_name("sDC_Code_Roof_Geo")).select_by_visible_text(kwargs['RoofGeometry'])

        Select(driver.find_element_by_name("sDC_Code_Building_Type")).select_by_visible_text(kwargs['DwellingType'])
        if kwargs['DwellingType'] == 'Rowhouse' or kwargs['DwellingType'] == 'Townhouse':
            Select(driver.find_element_by_name("sDC_Code_Num_Units")).select_by_visible_text(kwargs['NumberofUnits'])

        Select(driver.find_element_by_name("sDC_Code_Roof_Material")).select_by_visible_text(kwargs['RoofMaterialType'])
        if kwargs['ProtectionClass'] == '10':
            Select(driver.find_element_by_name("sDC_Code_Permitted_SubDivision")).select_by_visible_text(kwargs['PermittedSubdivision'])
            driver.execute_script("$('#sDC_Code_Permitted_SubDivision').change()")

        Select(driver.find_element_by_name("sDC_Code_Num_Families")).select_by_visible_text(kwargs['NumberofFamilies'])
        Select(driver.find_element_by_name("sDC_Code_Num_Stories")).select_by_visible_text(kwargs['NumberofStories'])
        Select(driver.find_element_by_name("sDC_Code_Num_Boarders")).select_by_visible_text(kwargs['NumberofBoarders'])

        driver.find_element_by_name("PQLI_SquareFeet").send_keys(kwargs['SquareFootage'])
        floodzone_list = driver.find_elements_by_name("PQLI_FloodZone")
        floodzone_list[0].clear()
        floodzone_list[0].send_keys(kwargs['FloodZone'])

        territory_list = driver.find_elements_by_name("sTER_Code")
        distanceToCoast_list = driver.find_elements_by_name("PQLI_DIST_ID")
        bceg_list = driver.find_elements_by_name("PQLI_BCEG_IndGrade")
        tierGroup_list = driver.find_elements_by_name("TierGroup")
        Select(territory_list[1]).select_by_visible_text(kwargs['Territory'])
        Select(distanceToCoast_list[1]).select_by_visible_text(kwargs['DistanceToCoast'])
        Select(bceg_list[1]).select_by_visible_text(kwargs['BCEG'])
        Select(tierGroup_list[1]).select_by_visible_text(kwargs['TierGroup'])

        Select(driver.find_element_by_name("sDC_Code_Primary_HeatSrc")).select_by_visible_text(kwargs['PrimaryHeatSource'])

        fuelStorageTanks_list = driver.find_elements_by_name("PQLI_FuelStorageTanks")
        if kwargs['TansksOnPremises'] == 'No':
            fuelStorageTanks_list[1].click()
        else:
            fuelStorageTanks_list[0].click()

        driver.find_element_by_name('Continue').click()
        print('--- Leave the application_page2')
        return 1
    else:
        return 0


def application_page3(driver, **kwargs):
    if check_timeout(driver, 'PQLI_CurAddYr', By.NAME) == 1:
        print('Enter into the application_page3 ---')
        driver.find_element_by_name('PQLI_CurAddYr').send_keys(kwargs['CurrentAddressYears'])

        mailingaddr_list = driver.find_elements_by_name("PQ_AddressSame")
        if kwargs['MailingAddrSameAsProperty'] == 'No':
            mailingaddr_list[1].click()
        else:
            mailingaddr_list[0].click()

        if kwargs['IsNewPurch'] == 'No':
            driver.find_element_by_name('PQLI_CurCarrier').send_keys(kwargs['CurrentCarrier'])
            driver.find_element_by_name('PQLI_CurExpDate').send_keys(kwargs['ExpirationDateForCurrentPolicy'])
            driver.find_element_by_name('PQLI_CurCarrierYrs').send_keys(kwargs['YearsWithCurrentCarrier'])

        if kwargs['PropertyInFloodZone'] == '1':
            driver.execute_script("$('#PropertyInFloodZone').click()")
            floodIns_list = driver.find_elements_by_name("PQLI_HasFloodIns")
            if kwargs['HasFloodIns'] == 'No':
                floodIns_list[1].click()
            else:
                floodIns_list[0].click()
                driver.find_element_by_name('PQLI_CurFloodCarrier').send_keys(kwargs['Flood_CurrentCarrier'])
                driver.find_element_by_name('PQLI_CurFloodExpDate').send_keys(kwargs['Flood_ExpirationDateForCurrentPolicy'])
                driver.find_element_by_name('PQLI_CurFloodCarrierYrs').send_keys(kwargs['Flood_YearsWithCurrentCarrier'])

        driver.find_element_by_name('Continue').click()
        print('--- Leave the application_page3')
        return 1
    else:
        return 0


def application_page4(driver, **kwargs):
    if check_timeout(driver, 'popup_ok', By.ID) == 1:
        print('Enter into the application_page4 ---')
        driver.find_element_by_id("popup_ok").click()
        if kwargs['LOB'] == '2' and kwargs['FRM'] == '12':
            driver.find_element_by_id("PQLI_CovALimit").clear()
            driver.find_element_by_name('PQLI_CovALimit').send_keys(kwargs['A'])
            driver.execute_script("$('#PQLI_CovALimit').change()")
            time.sleep(1)
            Select(driver.find_element_by_name("COV_Code_CovE")).select_by_visible_text(kwargs['E'])
            Select(driver.find_element_by_name("COV_Code_CovF")).select_by_visible_text(kwargs['F'])
            Select(driver.find_element_by_name("sDC_Code_Hurr_Deduct")).select_by_visible_text(kwargs['HurricaneDeductible'])
            Select(driver.find_element_by_name("sDC_Code_AO_Deduct")).select_by_visible_text(kwargs['AllOtherPerilsDeductible'])
        # else:
        #     driver.find_element_by_id("PQLI_CovALimit").clear()
        #     driver.find_element_by_name('PQLI_CovALimit').send_keys(kwargs['A'])
        #     Select(driver.find_element_by_name("PQLI_CovBLimit")).select_by_visible_text(kwargs['B'])
        #     driver.find_element_by_name('PQLI_CovCLimit').send_keys(kwargs['C'])
        #     driver.find_element_by_name('PQLI_CovDLimit').send_keys(kwargs['D'])

        '''Wind Mitigation section not enter values'''

        time.sleep(1)
        driver.execute_script("$('#Continue').click()")
        print('--- Leave the application_page4')
        return 1
    else:
        return 0


def application_page5(driver, **kwargs):
    print('Enter into the application_page5 ---')

    '''Option Coverage added'''
    for OptCoverage in kwargs['OptCoverage']:
        if OptCoverage != '':
            if check_timeout(driver, OptCoverage, By.LINK_TEXT) == 1:
                driver.find_element_by_link_text(OptCoverage).click()
                if check_timeout(driver, 'UpdateEndorsement', By.NAME) == 1:
                    driver.find_element_by_name('UpdateEndorsement').click()

    time.sleep(2)
    driver.find_element_by_name('Continue').click()
    print('--- Leave the application_page5')
    return 1


def application_page6(driver, **kwargs):
    time.sleep(5)
    print('Enter into the application_page6 ---')
    input_list = driver.find_elements_by_tag_name('input')
    for question in input_list:
        if question.get_attribute('type') == 'radio':
            qradio_list = driver.find_elements_by_name(question.get_attribute('name'))
            if kwargs['UWQuestion_result'] == 'No':
                if qradio_list[1].is_displayed():
                    qradio_list[1].click()
            else:
                if qradio_list[0].is_displayed():
                    qradio_list[0].click()
                # need add some other data

    time.sleep(1)
    driver.execute_script("$('#Continue').click()")
    time.sleep(10)
    print('--- Leave the application_page6')
    return 1


def application_page7(driver, **kwargs):
    print('Enter into the application_page7 ---')
    driver.find_element_by_name('Continue').click()
    time.sleep(1)
    print('--- Leave the application_page7')
    return 1


def application_page8(driver, **kwargs):
    if check_timeout(driver, 'PQ_TermInvoice', By.NAME) == 1:
        print('Enter into the application_page8 ---')
        driver.execute_script("$('#PQ_TermInvoice option:eq(0)').attr('disabled',true);")
        driver.execute_script("$('#PQ_RenewalInvoice option:eq(0)').attr('disabled',true);")
        # driver.find_element_by_name('paymentType').click()
        payment_list = driver.find_elements_by_name('NONEFT_PPL_ID')
        payment_list[0].click()  # Total Premium Payment

        # Check rating premium
        path_str = '//*[@id="rightColumn"]/div[6]'
        if check_timeout(driver, path_str + '/div[2]/label', By.XPATH) == 1:
            screen_premium = driver.find_element_by_xpath(path_str + '/div[2]/label').text

        if check_timeout(driver, path_str + '/div[4]/label', By.XPATH) == 1:
            screen_Fee = driver.find_element_by_xpath(path_str + '/div[4]/label').text

        if check_timeout(driver, path_str + '/div[8]/label', By.XPATH) == 1:
            screen_Surcharge = driver.find_element_by_xpath(path_str + '/div[8]/label').text

        if check_timeout(driver, path_str + '/div[6]/label', By.XPATH) == 1:
            screen_total_premium = driver.find_element_by_xpath(path_str + '/div[6]/label').text

        flag = 1
        if format_money_to_int(screen_premium) == format_money_to_int(kwargs['Premium']):
            print('Premium correct: %s' % screen_premium)
        else:
            print('Premium error: %s' % screen_premium)
            flag = 0

        if format_money_to_int(screen_Fee) == format_money_to_int(kwargs['Fee']):
            print('Premium correct: %s' % screen_Fee)
        else:
            print('Premium error: %s' % screen_Fee)
            flag = 0

        if format_money_to_int(screen_Surcharge) == format_money_to_int(kwargs['Surcharge']):
            print('Premium correct: %s' % screen_Surcharge)
        else:
            print('Premium error: %s' % screen_Surcharge)
            flag = 0

        if format_money_to_int(screen_total_premium) == format_money_to_int(kwargs['Total_Premium']):
            print('Premium correct: %s' % screen_total_premium)
        else:
            print('Premium error: %s' % screen_total_premium)
            flag = 0

        quote_code = driver.find_element_by_xpath('//*[@id="rightColumn"]/div[1]/label').text

        if flag == 1:
            print('Success. - %s' % quote_code)
            if check_timeout(driver, 'HO_FullQuote_Results', By.NAME) == 1:
                driver.find_element_by_name('HO_FullQuote_Results').click()
        else:
            print('Error. - %s' % quote_code)

        time.sleep(10)
        print('--- Leave the application_page8 --------------- HO3 Auto test finished.')


def check_timeout(driver, element, find_type, timeout=100):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((find_type, element)))
        return 1
    except:
        return 0


def format_money_to_int(value):
    return int(value.replace('$', '').replace(',', '').replace('.00', ''))

if __name__ == "__main__":
    driver = setUp()
    try:
        login(driver)
        test_ho3(driver)
        # test_ho6(driver)
        # test_df3(driver)
    finally:
        # driver.quit()
        print('test is done...')
