import pandas as pd
from urllib.parse import urlparse





class AddLead:


    def __init__(self,page):
        self.page = page
        self.base_url = urlparse(page.url)
        self.base_url = self.base_url.scheme + '://' + self.base_url.hostname

        print('BASEURL: ' + self.base_url)

        data = pd.read_excel('/vericol/samplevericol.xlsx')

        self.testdict = data.to_dict()

        print(self.testdict)


    def navigate(self):
        '''navigate to people page'''

        self.page.goto(self.base_url + "/lead")
        self.page.wait_for_load_state('domcontentloaded')


        self.page.click("id=cp_master_lbtn_new")
        self.page.wait_for_load_state('domcontentloaded')

    def loadfromxl(self):


        for i in range(len(self.testdict['Salesforce ID'])):
            print(self.testdict['Salesforce ID'][i])

            #no way to enter salesforce ID as of yet from lead page
           # self.page.fill("id=",self.testdict['Salesforce ID'][i])


            print(self.testdict['Program Name'][i])
            self.page.fill("id=cp_master_txt_customer",self.testdict['Program Name'][i]+"CUST")

            #Fake Customer Name from Program Name
            self.page.fill("id=cp_master_txt_program_name",self.testdict['Program Name'][i])



            print(self.testdict['Lead Phase'][i])
            self.page.select_option("id=cp_master_drp_fk_lkp_lead_phase",label=self.testdict['Lead Phase'][i])


            print(self.testdict['Win Probability'][i])
            self.page.fill("id=cp_master_txt_win_probability",str(self.testdict['Win Probability'][i]))

            print(self.testdict['RFP Release Date'][i])

            self.page.fill("id=cp_master_txt_lead_date__rfp_release_date",value=str(self.testdict['RFP Release Date'][i]).split()[0])
            #self.page.fill("id=cp_master_txt_lead_date__rfp_release_date",value="2022-07-19")

            print(self.testdict['Submit Date'][i])
            self.page.fill("id=cp_master_txt_lead_date__submit_due_date",value=str(self.testdict['Submit Date'][i]).split()[0])

            print(self.testdict['Close Date'][i])
            self.page.fill("id=cp_master_txt_lead_date__award_date",value=str(self.testdict['Close Date'][i]).split()[0])

            print(self.testdict['Disposition'][i])

            print(self.testdict['Company Value'][i])
            self.page.fill("id=cp_master_txt_value_company", value=str(self.testdict['Company Value'][i]))

            print(self.testdict['Total Value'][i])
            self.page.fill("id=cp_master_txt_value_total", value=str(self.testdict['Total Value'][i]))

            print(self.testdict['Bid Prime'][i])
            self.page.fill("id=cp_master_txt_bid_prime", value=str(self.testdict['Bid Prime'][i]))

            print(self.testdict['Account Name'][i])
            self.page.fill("id=cp_master_txt_bid_prime", value=str(self.testdict['Bid Prime'][i]))

            print(self.testdict['Territory'][i])
            print(self.testdict['Capture Manager'][i])
            print(self.testdict['Lead SA'][i])
            print(self.testdict['Business Development'][i])

            self.page.click("id=cp_master_lbtn_save")

            assert self.page.wait_for_selector("id=cp_master_wuc_status_lbl_success")
            self.navigate()








