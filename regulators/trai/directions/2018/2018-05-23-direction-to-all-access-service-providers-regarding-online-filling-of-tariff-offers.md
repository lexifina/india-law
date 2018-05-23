---
title: "Direction to all Access Service Providers regarding online filling of tariff offers"
kind: "direction"
number: "303-2(1)/2017"
issued: "2018-05-23"
in_force: "2018-05-23"
issuer: "Telecom Regulatory Authority of India"
source_url: "https://www.trai.gov.in/release-publication/directions?page=4"
official_text: "https://www.trai.gov.in/sites/default/files/2024-09/direction_tsps.pdf"
text: "English text layer of the official PDF (pdftotext -layout); Hindi lines omitted"
---

# Direction to all Access Service Providers regarding online filling of tariff offers

~~~~                                                                  q~,.,

   TELECOM REGULATORY AUTHORITY OF INDIA                                 ~

      1-lffif ftx4>IX IGovernment of India                       ~         TRAI ~

                                                                           20 G rlO ea~s
                                                                                      i9'/:-201 )

                                                   New Delhi, the 23rd May, 2018

                                                         DIRECTION

Subject: Direction under section 13, read with section 11 of the Telecom
                Regulatory Authority of India Act, 1997 to all Access Service
                Providers regarding online filing of tariff offers.

F. No. 303-2(1)/2017-F&EA (Vol. II) - Whereas the Telecom Regulatory Authority
of India, [hereinafter referred to as the Authority], established under sub-section (1)
of section 3 of the Telecom Regulatory Authority of India Act, 1997 (24 of 1997) has
been entrusted with discharge of functions, inter alia, to regulate
telecommunication services; ensure compliance of the terms and condition of
licence; notify rates for telecommunication services; protect interest of the
consumers of telecommunication service;

2. And whereas clause 7, read with sub-clause (1) of clause 2, of the Telecom
Tariff Order, 1999, provides that all service providers shall report to the Authority
any new tariff for telecommunication services and/ or any changes therein within
seven working days from the date of implementation of the said tariff for
information and record of the Authority after conducting a self-check to ensure that
the tariff plans are consistent with the regulatory principles in all respects;

3. And whereas, in order to protect the interest of the consumers of the telecom
 services, the Authority has launched the Beta version of Online Tariff Filing Portal
 enabling the consumers to view tariff of all service providers and compare them;

 4. Now, therefore, in exercise of powers conferred upon it under section 13, read
 with section 11, of the Telecom Regulatory Authority of India Act, 1997 and to
 protect the interest of the consumers of telecom sector, the Authority hereby directs
 all the Access Service Providers to report to the Authority with effect from the
 30th June 2018, through XML API web-service, all the tariffs offered to the
 consumers, in addition to the existing Tariff Reporting requirements.

                                                                         ~
                                                                               Advisor (F&EA)

   To
             All Telecom Access Service Providers

~  ~  1fCA, ~  z;m;j ~ lWf, Mahanagar Doorsanchar Shawan, Jawahar Lal Nehru Marg

      (TF" fit;:c) m), ~ ~ I (Old Minto Road), New Delhi-110002

      ~I Fax: +91-11-23213294, ~~~~<ttt -;:jo/EPSX No.: +91-11-23664145

TRAI &Telecom Access Service Providers

Version: 6.2

              P a g e 1 | 39

                            Table of Contents

1. Purpose                                      Page 3
                                                Page 3
2. Processing Methodology                       Page 3
                                                Page 3
a. Step 1 : XML File Generation                 Page 4
                                                Page 4
b. Step 2 : Web Request Creation                Page 5
                                                Page 5
c. Step 3 : Web Request Authentication          Page 7
                                                Page 7
d. Step 4 :Validation Checks                    Page 9
                                               Page 34
e. Step 5 : Data Storage                       Page 36
                                               Page 37
f. Step 6 : Response to Web Request

3. Format of Record ID No.

4. Important Points for XML Generation

5. Annexure 1

6. Annexure 2

7. Annexure 3

8. Annexure 4

                                               P a g e 2 | 39

       XML API For Receiving Tariff Data From TSPs

Purpose
The purpose of this XML API is to enable TSPs to push their respective tariff data to
TRAI server in XML format. The data will be authenticated before it is stored in the
TRAI database. The framework will also implement a communication methodology
that will give TSPs information on the status of data submission. TSPs will be
provided with a URI to which they will push the data in the form of an XML file along
due authentication parameters.

Processing Methodology

Step 1 : XML File Generation
TSPs will generate an XML file as per the predefined format (details as per
annexure-1 later in the document). This should be a valid XML file whose structure
should be strictly as per the predefined format, with no missing or misspelled tags.
The sequence of tags should also be exactly as per the sequence in the predefined
format.

Step 2 : Web Request Creation
The TSPs will create a web request to call the allocated URI for pushing the tariff
data. Using this web request, the TSP will push the XML file as described in Step 1.
The method of the web request need to be specified as ‘POST’, and the content type
of the web request will need to be specified as ‘text/xml’.
For authentication purpose, each TSP will be provided with a user ID, password and
a unique authorization key. These three parameters need to be passed as the web
request headers. Failure to authenticate any of these three parameters will result in
the rejection of complete XML file. The TSPs will use this web request to pass the
XML file as a stream to the web request URI. The API will receive this data stream.
Following are the summary pointsfor the web request to be created by the TSP for
quick reference

    1. Method : ‘POST’
    3. Authentication Parameters (User ID, Password, Authorization Key)
    4. XML file to be passed as a web stream to the URI using the web request

                                                                                               P a g e 3 | 39

A typical web request structure would be like the one given below :
WebRequest R1
String URI=<TRAI API URI Path>
String XMLFile=<Path to the XML File generated by the TSP>
R1.Headers[“userid”] = <User ID provided by TRAI>
R1.Headers[“password”]=<Password provided by TRAI>
R1.Headers[“authkey”]=<Authorization key provided by TRAI>
R1.Method=”POST”

Step 3: Web Request Authentication
All requests for pushing tariff data from the TSP will be authenticated at the TRAI
side. The three authentication parameters of User ID, Password and Authentication-
Key which the TSPs will pass in the header of the web request will be gathered and
validated.
In case some discrepancy is found in the authentication parameters, the XML data
will be out-rightly rejected and the error description for the same will be passed as
the response to the web request, so that the corrective action can be taken at the
TSP end.
If no discrepancy is found in the authentication parameters, the XML data will
undergo the various validation checks before it is accepted into the TRAI database.

                                                                                               P a g e 4 | 39

Step 4 : Validation Checks
After the request is authenticated at TRAI server, the XML data pushed by the TSP
will be subjected to validations. The validation will be a two stage process.
In the first stage of validation checks, each record will be checked for referential
integrity, i.e. the standard fields like LSA name, TSP name, Type of Service, Unique
Record ID No., Launch / Revision / Correction / Withdrawal, Date of Reporting, Date
of Launch etc. will be checked.

The second stage of validation will involve checking tariff validations (e.g. For plans,
a maximum of 25 active plans per Circle each for GSM/LTE (Prepaid), CDMA
(Prepaid), GSM/LTE (Postpaid), CDMA(Postpaid), Fixed Line Plan(Prepaid), Fixed
Line Plan(Postpaid) will be allowed per TSPetc.).

In case a tariff has one or more errors, it will be added to the list of erroneous
records. This list will consist of Unique Record ID No. along with the name of field(s)
with error and the details of error encountered. A tariff will not be eligible for
acceptance into the TRAI database if it has one or more errors. Only those records
that are found to be valid for each and every validation checks will be pushed into
the TRAI database.

Step 5 : Data Storage
If a tariff record is found to be valid across all validation checks, it will be pushed into
the TRAI database, and the status list will be updated accordingly. The status list will
be the response that will be sent back to web request raised by the TSPs to push the
data. When the iterative process of validating each record and storing the valid
records in the database is complete, TSPs will receive the complete status list as the
response to the web request.

                                                                                               P a g e 5 | 39

Step 6 : Response to Web Request

After the data storage process is completed, the system will pass the complete
status list as the response to the web request raised by the TSP. This status list will
enumerate all the Unique Record ID No’s pushed by the TSP, and against each
Unique Record ID No., it will be mentioned whether the particular record has been
accepted or rejected. In case of rejection, it will also mention the reason(s) for
rejection of the record.

The TSP can then make the required amendments to the erroneous records as per
the error report. After making the required changes to the tariff record, the TSP can
again push the data through the same process of creating a web request. There is
no restriction on the number of times a TSP can push the data to the TRAI server.

Format of Unique Record ID No.

The ‘Unique Record ID No.’ field for each tariff product should be a 12 digit unique
alphanumeric ID, which should follow the following format :

    1. The first two alphabets should be the TSP code, as per Annexure 3
    2. The next two alphabets should be the LSA code, as per Annexure 4
    3. The next four alphabets should be the Tariff Product Code, as per Annexure 2
    4. The last 4 digits should be numbers.

Important Points for XML Generation :

    1. As an exceptional case, if ‘Unlimited’ needs to be specified for a numeric
         attribute key value, the word ‘Unlimited’ can be written for that attribute key
         value. The required conversion will be done by the software at the time of
         validating the data.

    2. The date type attribute key values should be filled in the format “dd-MMM-
         yyyy” (e.g. 10th April 2018 should be entered as ’10-APR-2018’)

                                                                                               P a g e 6 | 39

3. For attribute keys where data is to be entered as time (e.g. “Time for Call
    Rates – Peak Time From”), it should be entered as “hh:mm:ss” in 24-hour
    format (e.g. 6:30 PM should be entered as “18:30:00”)

4. Annexure 1 provides the complete information towards the attribute keys for
    the XML generation at the TSP end. Following are the details about the
    Annexure 1 columns :
          Attribute Key – The key name as it is to be entered in the XML file.
          Attribute Description :Description of the data that each key refers to.
          Attribute Type : The data type of each key i.e. the kind of data that can
             be entered for each attribute key.
          Valid Values : Details about what is to be filled in each attribute key
          Applicable for : The various tariff product types for which the attribute
             key is to be filled. E.g. for a ‘Combo Pack’ type tariff product, the
             attribute key A8 (category) is not applicable. Hence this attribute key
             needs to be kept in the XML file without any value.

5. The following regulatory requirements need to be fulfilled by a tariff product
    before it is considered eligible for storage in TRAI database.

          All tariff launch or revision needs to be reported within 7 working days –
             both the days on which the tariff is reported and implemented are to be
             excluded while calculating 7 working days

          ‘Top-Up’ vouchers should be in multiples of Rs. 10 only – can offer only
             monetary value without any validity or usage restriction

          STV should not be offered in multiples of Rs. 10 -should contain only
             tariff benefits & no monetary value - validity should not be more than 90
             days, unless it is an STV providing exclusive data benefits.

          Combo Vouchers should not be offered in multiples of Rs. 10 – it offers
             monetary value in addition to other benefits

          Validity of STV/ CV can be maximum for 90days. However, forSTV with
             “data only” benefits, maximum validity is 365 days.

          For plans, a maximum of 25 active plansper Circleeach for GSM/LTE
             (Prepaid), CDMA (Prepaid), GSM/LTE (Postpaid), CDMA(Postpaid),
             Fixed Line Plan(Prepaid), Fixed Line Plan(Postpaid) will be allowed
             per TSP. Exceeding this limit while submission will render a record
             invalid

          Correction of any tariff product is allowed within 2 days only& reason
             for correction needs to be compulsory mentioned in remarks column
             no. A268 as per annexure 1.

                                                                                          P a g e 7 | 39

            Details mentioned in tariff summary needs to be mentioned somewhere
               in other data fields also e.g: Remark / Conditions field.

Annexure 1
Attributes for XML file to be generated by the TSPs

Attribute           Attribute Description       Attribute Type         Valid Values         Applicable
   Key                                          Alphanumeric                                     For
           Tariff ProductType, as per Annexure                  Name of the Tariff Type.
A1         2                                                                              All Tariff
                                                                Should be in a pre-       Product Types
                                                                defined value format as
                                                                per column “Tariff
                                                                Product Type” of
                                                                Annexure 2.

A2         Tariff Summary                       Alphanumeric    This is a compulsory      All Tariff
                                                                field.                    Product Types
                                                                - Text detail describing
                                                                the tariff product

                                                                - Details mentioned in
                                                                tariff summary needs
                                                                to be mentioned
                                                                somewhere in other
                                                                data fields also e.g:
                                                                Remark / Conditions
                                                                field

                                                                This is a compulsory

                                                                field.

A3         Unique Record ID No. of each tariff Alphanumeric A unique identifier.          All Tariff

           product.                                                                       Product Types

                                                                Refer Annexure 2, 3 & 4

                                                                for the standard format.

                                                                This is a compulsory

                                                                field.

A4         Respective TSP Name, as per          Alphanumeric Name of the TSP.             All Tariff

           Annexure 3                                                                     Product Types

                                                                Should be in a pre-

                                                                defined value format as

                                                                per column “TSP

                                                                Names” of Annexure 3.

                                                                This is a compulsory
                                                                field.

A5         LSA (Licensed Service Area), as per Alphanumeric Licensed Service Area All Tariff

           Annexure 4                                           Name                      Product Types

                                                                Should be in a pre-
                                                                defined value format as
                                                                per column “LSA
                                                                Names” of Annexure 4.

                                                                This is a compulsory

                                                                                          P a g e 8 | 39

                                                     field.

A6   SSA / Cities (In which Services   Alphanumeric Names of Cities where For ISP only

     available)                                      service is available

A7   Type of Service                   Alphanumeric  For Fixed Line Plan,        All Tariff
                                                     Fixed Line WLL Plan&        Product Types
                                                     Fixed Line Add On Pack      except ISP
                                                     – Any one option from
                                                     :Landline/
                                                     Broadband/Both

                                                     For Others, any one
                                                     option from : GSM /
                                                     CDMA / LTE

                                                     For plans, a maximum
                                                     of 25 active plans per
                                                     Circle each for
                                                     GSM/LTE (Prepaid),
                                                     CDMA (Prepaid),
                                                     GSM/LTE (Postpaid),
                                                     CDMA(Postpaid), Fixed
                                                     Line Plan(Prepaid),
                                                     Fixed Line
                                                     Plan(Postpaid) will be
                                                     allowed per TSP.
                                                     Exceeding this limit
                                                     while submission will
                                                     render a record invalid

A8   Prepaid / Postpaid                Alphanumeric  This is a compulsory        All Tariff
                                                     field.                      Product Types
                                                     any one option from :
                                                     Prepaid / Postpaid

                                                     This is a compulsory

                                                     field.

A9   Launch / Revision / Correction /  Alphanumeric Any one option from : All Tariff

     Withdrawal                                      Launch / Revision /         Product Types

                                                     Correction / Withdrawal

                                                     For plans, a maximum
                                                     of 25 active plans per
                                                     Circle each for
                                                     GST/LTE (Prepaid),
                                                     CDMA (Prepaid),
                                                     GSM/LTE (Postpaid),
                                                     CDMA(Postpaid), Fixed
                                                     Line Plan(Prepaid),
                                                     Fixed Line
                                                     Plan(Postpaid) will be
                                                     allowed per TSP

                                                     - Correction of any tariff
                                                     product is allowed
                                                     within 2 days only

                                                     - If ‘Correction’, reason
                                                     for correction needs to
                                                     be compulsory
                                                     mentioned in remarks
                                                     column no. A268 as per
                                                     annexure 1

                                                     This is a compulsory

                                                     field.

A10  Revision Unique Record ID No. of  Alphanumeric  A unique identifier         All Tariff

                                                                            P a g e 9 | 39

     the revised tariff product.                    Refer Annexure 2, 3 & 4 Product Types
                                                    for the standard format.

                                                    It should be different
                                                    from the original tariff
                                                    product’s unique record
                                                    ID No.

                                                    This field is compulsory

                                                    if it’s a ‘Revision’

                                                    Record.

A11  Name of the Product              Alphanumeric The name given to the All Tariff

                                                    product by the TSP        Product Types

                                                                              except :

                                                    This is a compulsory      Gen ISD Tariff

                                                    field.                    &

                                                                              International

                                                                              Roaming

A12  Unique Plan ID of the Voucher / of Alphanumeric If there is a unique Plan Applicable

     the plans for which exclusively                ID of the voucher given only for Plan

     applicable                                     by the TSP, it needs to Voucher &

                                                    be specified here         Postpaid Plan

A13  Date of Reporting                Date          For plans, a maximum      All Tariff
                                                    of 25 active plans per    Product Types
                                                    Circle each for
                                                    GST/LTE (Prepaid),
                                                    CDMA (Prepaid),
                                                    GSM/LTE (Postpaid),
                                                    CDMA(Postpaid), Fixed
                                                    Line Plan(Prepaid),
                                                    Fixed Line
                                                    Plan(Postpaid) will be
                                                    allowed per TSP
                                                    Date on which the tariff
                                                    product was reported to
                                                    TRAI. Needs to be a
                                                    valid date not greater
                                                    than the current date.

                                                    Date needs to be in “dd-
                                                    MMM-yyyy” format.

A14  Date of Launch / Revision /      Date          This is a compulsory      All Tariff
                                                    field.                    Product Types
     Correction / Withdrawal
                                                    Date on which the tariff
                                                    product was actually
                                                    launched / revised /
                                                    corrected / withdrawn
                                                    by the TSP

                                                    Date in this field needs
                                                    to be less than or equal
                                                    to A13

                                                    Date needs to be in “dd-
                                                    MMM-yyyy” format.

A15  Regular / Promotional            Alphanumeric  This is a compulsory      All Tariff
                                                    field.                    Product Types
                                                                              except :
                                                    This field specifies
                                                    whether the tariff        Promo Offer
                                                    product is a regular
                                                    offer or a promotional
                                                    offer. TSP needs to fill
                                                    either ‘Regular’ or

                                                                          P a g e 10 | 39

A16  Start date of Promotional offer  Alphanumeric  ‘Promotional’ in this      Gen ISD Tariff
                                      Alphanumeric  field.
                                                                               International
                                                    This is a compulsory       Roaming
                                                    field.
                                                    Starting date of the       All Tariff
                                                    promotional offer.         Product Types
                                                                               except :
                                                    If applicable, Date        Gen ISD Tariff
                                                    needs to be in “dd-        &
                                                    MMM-yyyy” format.          International
                                                                               Roaming
                                                    Validity of STV / CV can
                                                    be maximum for
                                                    90days. However, for
                                                    STV with “data only”
                                                    benefits, maximum
                                                    validity is 365 days.

A17  End date of Promotional offer                  This is a compulsory       All Tariff
                                                    field if A15 is            Product Types
                                                    ‘Promotional’              except :
                                                    Ending date of the         Gen ISD Tariff
                                                    promotional offer.         &
                                                                               International
                                                    If Applicable, Date        Roaming
                                                    needs to be in “dd-
                                                    MMM-yyyy” format.

                                                    Validity of STV / CV can
                                                    be maximum for
                                                    90days. However, for
                                                    STV with “data only”
                                                    benefits, maximum
                                                    validity is 365 days.

                                                    Date in this field needs
                                                    to be greater than or
                                                    equal to A16

                                                    This is a compulsory

                                                    field if A15 is

                                                    ‘Promotional’

A18  special Eligibility Conditions, if any Alphanumeric If no eligibility condition All Tariff

                                                    applicable, then “NIL” Product Types

                                                    should be entered in

                                                    this field.

A19  Price (Including Processing Fee & Numeric      This is a compulsory       Prepaid Plan
                                                    field.                     Voucher
     GST) /                                         A numeric non-negative
                                                    value denoting the Price   Prepaid STV
                                                    (Including Processing
                                                    Fee & GST).

                                                    ‘Top-Up’ vouchers          Prepaid
                                                    should be in multiples of  Combo
                                                    Rs. 10 only
                                                                               Prepaid Top
                                                    STV & Combo                Up
                                                    Vouchers should not be
                                                    in multiples of Rs. 10     Prepaid VAS

                                                                                        Prepaid
                                                    This field is compulsory Promo Offer

                                                                          P a g e 11 | 39

                                                   for Prepaid Plan

                                                   Voucher, Prepaid STV, SUK

                                                   Prepaid Combo,

                                                   Prepaid Top Up,             ISP

                                                   Prepaid VAS, SUK, ISP

A20  Monetary Value (in Rs.)              Numeric  The monetary value          Prepaid

                                                   benefit that will be given Combo

                                                   to the consumer

                                                                               Prepaid Top

                                                                               Up

                                                   This is a compulsory

                                                   field.

                                                                            -

A21  Available in (Rural / Urban/ Both /  Alphanumeric Specify whether the     Fixed Line

     Any other)                                    plan is available in        Plan

                                                   Rural / Urban/ Both /

                                                   Any other                   Fixed Line

                                                                               WLL Plan

                                                                               Fixed Line
                                                                               Add On Pack

A22  Registration charges                 Numeric  Amount of registration      Fixed Line
                                                   charges, if any             Plan

                                                                               Fixed Line
                                                                               WLL Plan

A23  Installation / activation charges    Numeric  Amount of Installation      Fixed Line
                                                   Charges / Activation        Add On Pack
                                                   Charges, if any
                                                                               ISP

                                                                               Postpaid Plan
                                                                               Fixed Line
                                                                               Plan

                                                                               Fixed Line
                                                                               WLL Plan

                                                                               Fixed Line
                                                                               Add On Pack

                                                                               ISP

A24  One time Security Deposit            Numeric  Amount of ISP Deposit,      Postpaid Plan
                                          Numeric  if any                      ISP
A25  Normal Modem Charges                 Numeric  Normal Modem
                                          Numeric  charges, if any             ISP
A26  WiFi Modem Charges                                                        Fixed Line
                                                   Wifi Modem Charges, if      Plan
A27  Plan enrolment fee, if any                    any                         ISP
                                                                               Fixed Line
                                                   Enrolment fee for the       Plan
                                                   plan, if any                Fixed Line
                                                                               Plan

                                                                               Fixed Line
                                                                               WLL Plan

                                                                               Fixed Line
                                                                               Add On Pack

                                                                            P a g e 12 | 39

A28  Other one time charges (Please    Numeric    Any other charges         ISP

     specify)                                                               Postpaid Plan
                                                                            Fixed Line
                                                                            Plan

                                                                            Fixed Line
                                                                            WLL Plan

                                                                            Fixed Line
                                                                            Add On Pack

                                                                            ISP

A29  Rental / Minimum billing amount, if Numeric  Rental or minimum         Postpaid Plan
                                                  billing amount, if any.   ISP
     any- Fixed Charges
                                                  This field is compulsory  Postpaid Plan
                                                  for ISP, Postpaid Plan,
                                                  Postpaid Add On Pack,     Postpaid Add
                                                  Fixed Line Plan, Fixed    On Pack
                                                  Line WLL Plan, Fixed
                                                  Line Add On Pack          Postpaid

                                                                            Promo Offer

                                                                            Fixed Line
                                                                            Plan

                                                                            Fixed Line
                                                                            WLL Plan

A30  Advance rental option for longer             Advance rental amount,    Fixed Line
                                                  if any                    Add On Pack
     periods                           Numeric                              ISP

                                                                            Postpaid Plan

                                                                            Fixed Line
                                                                            Plan

                                                                            Fixed Line
                                                                            WLL Plan

A31  Security Deposit - Local          Numeric    Amount of Security        Fixed Line
                                                  Deposit - Local           Add On Pack
                                                                            Postpaid Plan

                                                                            Fixed Line
                                                                            Plan

                                                                            Fixed Line
                                                                            WLL Plan

A32  Security Deposit – Local + STD    Numeric    Amount of Security        Fixed Line
                                                  Deposit – Local + STD     Add On Pack
                                                                            Postpaid Plan

                                                                            Fixed Line
                                                                            Plan

                                                                            Fixed Line
                                                                            WLL Plan

                                                                      P a g e 13 | 39

A33  Security Deposit – Local + STD +  Numeric    Amount of Security       Fixed Line
                                                  Deposit – Local + STD    Add On Pack
     ISD                                          + ISD                    Postpaid Plan

                                                                           Fixed Line
                                                                           Plan

                                                                           Fixed Line
                                                                           WLL Plan

A34  Security Deposit – National Roaming Numeric  Amount of Security       Fixed Line
                                                  Deposit – National       Add On Pack
A35  Security Deposit – International  Numeric    Roaming                  Postpaid Plan

                                                  Amount of Security       Postpaid Plan
                                                  Deposit – International
     Roaming                                      Roaming

A36  Security Deposit – Any Other      Numeric    Amount of Security       Postpaid Plan
                                                  Deposit – Any other
                                                                           Fixed Line
                                                                           Plan

                                                                           Fixed Line
                                                                           WLL Plan

A37  Fixed Charges –Exchange           Numeric    If Exchange capacity     Fixed Line
                                                  wise FMC (Charges for    Add On Pack
     Capacity<=999                                exchange capacity        Fixed Line
                                                  <=999)                   Plan

                                                                           Fixed Line
                                                                           WLL Plan

A38  Fixed Charges –Exchange Capacity Numeric     If Exchange capacity     Fixed Line
                                                  wise FMC(Charges for     Add On Pack
     > 999 and <=29999                            exchange capacity>       Fixed Line
                                                  999 and <=29999)         Plan
A39  Fixed Charges –Exchange Capacity Numeric
                                                  If Exchange capacity     Fixed Line
     >= 30000 and <=99999                         wise FMC(Charges for     WLL Plan
                                                  exchange capacity >=
A40  Fixed Charges –Exchange Capacity Numeric     30000 and <=99999)       Fixed Line
                                                                           Add On Pack
     >= 100000                                    If Exchange capacity     Fixed Line
                                                  wise FMC(Charges for     Plan
                                                  exchange capacity >=
                                                  100000)                  Fixed Line
                                                                           WLL Plan

                                                                           Fixed Line
                                                                           Add On Pack
                                                                           Fixed Line
                                                                           Plan

                                                                           Fixed Line
                                                                           WLL Plan

                                                                           Fixed Line
                                                                           Add On Pack

                                                                       P a g e 14 | 39

A41  Optional Fixed Monthly Charges -  Numeric  CLIP Charges               Fixed Line
                                                                           Plan
     CLIP
                                                                           Fixed Line
                                                                           WLL Plan

                                                                           Fixed Line
                                                                           Add On Pack

A42  Free Calls – MCUS per month       Numeric  Free calls in MCUS per Fixed Line

                                                month                      Plan

                                                                           Fixed Line
                                                                           WLL Plan

A43  Free Calls – MCUS per month –     Numeric  Free calls in MCUS per     Fixed Line
                                                month for exchange         Add On Pack
     Exchange capacity<=999                     capacity <=999             Fixed Line
                                                                           Plan

                                                                           Fixed Line
                                                                           WLL Plan

A44  Free Calls – MCUS per month –     Numeric  Free calls in MCUS per     Fixed Line
                                                month for exchange         Add On Pack
     Exchange capacity> 999 and                 capacity> 999 and          Fixed Line
                                                <=29999                    Plan
     <=29999
                                                                           Fixed Line
                                                                           WLL Plan

A45  Free Calls – MCUS per month –     Numeric  Free calls in MCUS per     Fixed Line
                                                month for exchange         Add On Pack
     Exchange capacity>=30000 and               capacity >= 30000 and      Fixed Line
                                                <=99999                    Plan
     <=99999
                                                                           Fixed Line
                                                                           WLL Plan

A46  Free Calls – MCUS per month –     Numeric  Free calls in MCUS per     Fixed Line
                                                month for exchange         Add On Pack
     Exchange capacity >= 100000                capacity >= 100000         Fixed Line
                                                                           Plan

                                                                           Fixed Line
                                                                           WLL Plan

A47  Free Calls – MCUS per month –     Numeric  Free talktime in Rs. (per  Fixed Line
                                                month) :                   Add On Pack
     Free Talktime                                                         Fixed Line
                                                                           Plan

                                                                           Fixed Line
                                                                           WLL Plan

A48  Validity                          Numeric  Validity ( in days)        Fixed Line
                                                                           Add On Pack
                                                For STV / CV, validity     All Tariff
                                                can be maximum90           Product Types
                                                days.                      except :

                                                For STV with “data only”   Prepaid Top
                                                benefits, maximum          Up
                                                validity is 365 days.
                                                                           Gen ISD Tariff

                                                              P a g e 15 | 39

A49  Pay Per Use charges                  Alphanumeric  Pay per use model          International
                                          Alphanumeric  (Usage charges)            Roaming
A50  Other Model – Details                Alphanumeric                             Prepaid VAS
                                                        Any other model
A51  Benefits                                           (Details)                  Postpaid VAS
                                                                                   Prepaid VAS
                                                        Benefits of the service
                                                                                   Postpaid VAS
                                                                                   Prepaid VAS

                                                                                   Promo Offer

                                                                                   Postpaid VAS

A52  Call Rates – Peak Time From, if any Alphanumeric Peak Time From which Prepaid Plan

                                                        call rates applicable      Voucher

A53  Call Rates – Peak Time Till, if any  Alphanumeric  Peak Time till which call

                                                        rates applicable           Prepaid STV

A54  Call Rates – Off Peak Time From, if Alphanumeric Off Peak Time From

     any                                                which call rates           Prepaid

                                                        applicable                 Combo

A55  Call Rates – Off Peak Time Till, if  Alphanumeric Off Peak Time Till which

     any                                                call rates applicable      SUK

                                                                                   Postpaid Plan

                                                                                   Postpaid Add
                                                                                   On Pack

                                                                                   Fixed Line
                                                                                   Plan

                                                                                   Fixed Line
                                                                                   WLL Plan

                                                                                   Fixed Line
                                                                                   Add On Pack

A56  All Local Call (Onnet + Offnet +     Numeric       Voice pulse for All local  Prepaid Plan
                                                        call (Onnet + Offnet +     voucher
     Peak + Offpeak) – Voice Pulse (in                  Peak + Offpeak)
                                                        Video pulse for All local  Prepaid STV
     seconds)                                           call (Onnet + Offnet +
                                                        Peak + Offpeak)            Prepaid
A57  All Local Call (Onnet + Offnet +     Numeric       Voice Call Rate for All    Combo
                                                        local call rate (Onnet +
     Peak + Offpeak) – Video Pulse (in                  Offnet + Peak +            SUK
                                                        Offpeak)
     seconds)                                           Video Call Rate for All    Postpaid Plan
                                                        local call rate (Onnet +
A58  All Local Call Rate (Onnet + Offnet + Numeric      Offnet + Peak +            Postpaid Add
                                                        Offpeak)                   On Pack
     Peak + Offpeak) -

     Voice Call Rate (in INR/pulse)

A59  All Local Call Rate (Onnet + Offnet + Numeric

     Peak + Offpeak) -

     Video Call Rate (in INR/pulse)

                                                                                   Fixed Line
                                                                                   Plan

                                                                                   Fixed Line
                                                                                   WLL Plan

                                                                                   Fixed Line
                                                                                   Add On Pack

A60  Local Call MobileOnNet -             Numeric       Parameters for             Prepaid Plan
                                          Numeric       Local Call Rate            voucher
     Voice Pulse(in seconds)                            MobileOnNet
                                                                                   Prepaid STV
A61  Local Call MobileOnNet -                           Parameters for
                                                        Local Call Rate            Prepaid
     Video Pulse(in seconds)

                                                                               P a g e 16 | 39

                                                 MobileOnNet              Combo

A62  Local Call Rate MobileOnNet -      Numeric

     Voice Call Rate (Peak Hrs)(in                                        SUK

     INR/pulse)

                                                                          Postpaid Plan

A63  Local Call Rate MobileOnNet -      Numeric

     Video Call Rate (Peak Hrs)(in                                        Postpaid Add
                                                                          On Pack
     INR/pulse)

A64  Local Call Rate MobileOnNet -      Numeric

     Voice Call Rate (off peak Hrs)(in                                    Fixed Line
                                                                          Plan
     INR/pulse)                                                           Fixed Line
                                                                          WLL Plan
A65  Local Call Rate Mobile OnNet -     Numeric

     Video Call Rate (off Peak Hrs)(in

     INR/pulse)                                                           Fixed Line
                                                                          Add On Pack

A66  Local Call MobileOnNet -           Numeric  Local Call MobileOnNet   Prepaid STV
                                                 -
     Validity in Days                            Validity in Days         Prepaid
                                                                          Combo
A67  Local Call MobileOffNet -          Numeric  Parameters for           Prepaid Plan
                                                 Local Call Rate          voucher
     Voice Pulse(in seconds)                     MobileOffNet
                                                                          Prepaid STV
A68  Local Call MobileOffNet -          Numeric

     Video Pulse(in seconds)

A69  Local Call Rate MobileOffNet -     Numeric                           Prepaid
                                                                          Combo

     Voice Call Rate (Peak Hrs)(in

     INR/pulse)                                                           SUK

A70  Local Call Rate MobileOffNet -     Numeric                           Postpaid Plan

     Video Call Rate (Peak Hrs)(in

     INR/pulse)                                                           Postpaid Add
                                                                          On Pack

A71  Local Call Rate MobileOffNet -     Numeric                           Fixed Line
                                                                          Plan
     Voice Call Rate (off peak Hrs)(in

     INR/pulse)

A72  Local Call Rate MobileOffNet -     Numeric                           Fixed Line
                                                                          WLL Plan
     Video Call Rate (off Peak Hrs)(in

     INR/pulse)                                                           Fixed Line
                                                                          Add On Pack

A73  Local Call MobileOffNet -          Numeric  Local Call MobileOffNet  Prepaid STV
                                                 -
     Validity in Days                            Validity in Days         Prepaid
                                                                          Combo
A74  Local Call Fixed OnNet -           Numeric  Parameters for           Prepaid Plan
                                                 Local Call Rate Fixed    voucher
     Voice Pulse(in seconds)                     OnNet
                                                                          Prepaid STV
A75  Local Call Fixed OnNet -           Numeric

     Video Pulse(in seconds)

A76  Local Call Rate Fixed OnNet -      Numeric                           Prepaid
                                                                          Combo

     Voice Call Rate (Peak Hrs)(in

     INR/pulse)                                                           SUK

A77  Local Call Rate Fixed OnNet -      Numeric                           Postpaid Plan

     Video Call Rate (Peak Hrs)(in

     INR/pulse)                                                           Postpaid Add
                                                                          On Pack

A78  Local Call Rate Fixed OnNet -      Numeric                           Fixed Line
                                                                          Plan
     Voice Call Rate (off peak Hrs)(in

     INR/pulse)

                                                              P a g e 17 | 39

A79  Local Call Rate Fixed OnNet -       Numeric                                    Fixed Line
                                                                                    WLL Plan
     Video Call Rate (off Peak Hrs) (in
                                                                                    Fixed Line
     INR/pulse)                                                                     Add On Pack

A80  Local Call Fixed OnNet -            Numeric  Local Call Fixed OnNet            Prepaid STV
                                                  - Validity
     Validity in Days                    Numeric                                    Prepaid
                                         Numeric  Parameters for                    Combo
A81  Local Call MobileOffNet -           Numeric  Local Call Rate Fixed             Prepaid Plan
                                                  OffNet                            voucher
     Voice Pulse(in seconds)
                                                                                    Prepaid STV

     Video Pulse(in seconds)

A83  Local Call Rate MobileOffNet -                                                 Prepaid
                                                                                    Combo

     Voice Call Rate (Peak Hrs)(in

     INR/pulse)                                                                     SUK

A84  Local Call Rate MobileOffNet -      Numeric                                    Postpaid Plan

     Video Call Rate (Peak Hrs)(in                                                  Postpaid Add
                                                                                    On Pack
     INR/pulse)
                                                                                    Fixed Line
A85  Local Call Rate MobileOffNet -      Numeric                                    Plan
                                                                                    Fixed Line
     Voice Call Rate (off peak Hrs)(in                                              WLL Plan

     INR/pulse)                                                                     Fixed Line
                                                                                    Add On Pack
A86  Local Call Rate MobileOffNet -      Numeric

     Video Call Rate (off Peak Hrs)(in

     INR/pulse)

A87  Local Call MobileOffNet -           Numeric  Local Call MobileOffNet           Prepaid STV
                                                  -
     Validity in Days                             Validity in Days                  Prepaid
                                                                                    Combo

A88  CUP (Commercial Usage Policy), if Alphanumeric CUP for Local Call rate Prepaid Plan

     any                                                                            voucher

A89  Description of local call rate / pulse Alphanumeric Description of local call

     rate in case any other pattern is            rate / pulse rate in case Prepaid STV

     followed                                     any other pattern is

                                                  followed                          Prepaid

                                                                                    Combo

                                                                                    SUK

                                                                                    Postpaid Plan

                                                                                    Postpaid Add
                                                                                    On Pack

                                                                                    Fixed Line
                                                                                    Plan

                                                                                    Fixed Line
                                                                                    WLL Plan

                                                                                    Fixed Line
                                                                                    Add On Pack

A90  All STD Call (Onnet + Offnet + Peak Numeric  Voice pulse for All STD           Prepaid Plan
                                                  call (Onnet + Offnet +            voucher
     + Offpeak) – Voice Pulse (in                 Peak + Offpeak)

     seconds)

                                                                        P a g e 18 | 39

A91   All STD Call (Onnet + Offnet + Peak Numeric  Video pulse for All STD  Prepaid STV
                                                   call (Onnet + Offnet +
      + Offpeak) – Video Pulse (in                 Peak + Offpeak)          Prepaid
                                                   Voice Call Rate for All  Combo
      seconds)                                     STD call rate (Onnet +
                                                   Offnet + Peak +          SUK
A92   All STD Call Rate (Onnet + Offnet + Numeric  Offpeak)
                                                   Video Call Rate for All  Postpaid Plan
      Peak + Offpeak) -                            STD call rate (Onnet +
                                                   Offnet + Peak +          Postpaid Add
      Voice Call Rate (in INR/pulse)               Offpeak)                 On Pack

A93   All STD Call Rate (Onnet + Offnet + Numeric

      Peak + Offpeak) -

      Video Call Rate (in INR/pulse)

                                                                            Fixed Line
                                                                            Plan

                                                                            Fixed Line
                                                                            WLL Plan

                                                                            Fixed Line
                                                                            Add On Pack

A94   STD Call MobileOnNet -             Numeric   Parameters for           Prepaid Plan
A95   Voice Pulse(in seconds)            Numeric   STD Call RateMobile      voucher
A96                                      Numeric   OnNet
A97   STD Call MobileOnNet -             Numeric                            Prepaid STV
A98   Video Pulse(in seconds)            Numeric
A99                                      Numeric                            Prepaid
      STD Call Rate MobileOnNet -                                           Combo
A100  Voice Call Rate (Peak Hrs)(in      Numeric
      INR/pulse)                                                            SUK

      STD Call Rate MobileOnNet -                                           Postpaid Plan
      Video Call Rate (Peak Hrs)(in
      INR/pulse)                                                            Postpaid Add
                                                                            On Pack
      STD Call Rate MobileOnNet -
      Voice Call Rate (off peak Hrs)(in                                     Fixed Line
      INR/pulse)                                                            Plan
                                                                            Fixed Line
      STD Call Rate MobileOnNet -                                           WLL Plan
      Video Call Rate (off Peak Hrs)(in
      INR/pulse)                                                            Fixed Line
                                                                            Add On Pack
      Validity in Days                             STD Call MobileOnNet -   Prepaid STV
                                                   Validity in Days
                                                                            Prepaid
                                                                            Combo

A101  STD Call MobileOffNet -            Numeric   Parameters for           Prepaid Plan
A102  Voice Pulse(in seconds)            Numeric   STD Call Rate Mobile     voucher
A103                                     Numeric   OffNet
A104  STD Call MobileOffNet -            Numeric                            Prepaid STV
A105  Video Pulse(in seconds)            Numeric
                                                                            Prepaid
      STD Call Rate MobileOffNet -                                          Combo
      Voice Call Rate (Peak Hrs)(in
      INR/pulse)                                                            SUK

      STD Call Rate MobileOffNet -                                          Postpaid Plan
      Video Call Rate (Peak Hrs)(in
      INR/pulse)                                                            Postpaid Add
                                                                            On Pack
      STD Call Rate MobileOffNet -
      Voice Call Rate (off peak Hrs)(in                                     Fixed Line
      INR/pulse)                                                            Plan

                                                                         P a g e 19 | 39

A106  STD Call Rate MobileOffNet -       Numeric                                Fixed Line
      Video Call Rate (off Peak Hrs)(in  Numeric                                WLL Plan
A107  INR/pulse)
                                                       STD Call MobileOffNet -  Fixed Line
A108  STD Call MobileOffNet -                          Validity in Days         Add On Pack
A109  Validity in Days                                                          Prepaid STV
A110
A111                                                                            Prepaid
A112                                                                            Combo
A113
A114  STD Call Fixed OnNet -             Numeric       Parameters for           Prepaid Plan
      Voice Pulse(in seconds)            Numeric       STD Call Rate Fixed      voucher
A115                                     Numeric       OnNet
A116  STD Call Fixed OnNet -             Numeric                                Prepaid STV
A117  Video Pulse(in seconds)            Numeric
A118                                     Numeric                                Prepaid
A119  STD Call Rate Fixed OnNet -        Numeric                                Combo
A120  Voice Call Rate (Peak Hrs)(in
A121  INR/pulse)                                                                SUK

A122  STD Call Rate Fixed OnNet -                                               Postpaid Plan
      Video Call Rate (Peak Hrs)(in
      INR/pulse)                                                                Postpaid Add
                                                                                On Pack
      STD Call Rate Fixed OnNet -
      Voice Call Rate (off peak Hrs)(in                                         Fixed Line
      INR/pulse)                                                                Plan
                                                                                Fixed Line
      STD Call Rate Fixed OnNet -                                               WLL Plan
      Video Call Rate (off Peak Hrs)(in
      INR/pulse)                                       STD Call Fixed OnNet -   Fixed Line
                                                       Validity in Days         Add On Pack
      STD Call Fixed OnNet -                                                    Prepaid STV
      Validity in Days
                                                                                Prepaid
                                                                                Combo

      STD Call Fixed OffNet -            Numeric       Parameters for           Prepaid Plan
      Voice Pulse(in seconds)            Numeric       STD Call Rate Fixed      voucher
                                         Numeric       OffNet
      STD Call Fixed OffNet -            Numeric                                Prepaid STV
      Video Pulse(in seconds)            Numeric
                                         Numeric                                Prepaid
      STD Call Rate Fixed OffNet -       Numeric                                Combo
      Voice Call Rate (Peak Hrs)(in
      INR/pulse)                                                                SUK

      STD Call Rate Fixed OffNet -                                              Postpaid Plan
      Video Call Rate (Peak Hrs)(in
      INR/pulse)                                                                Postpaid Add
                                                                                On Pack
      STD Call Rate Fixed OffNet -
      Voice Call Rate (off peak Hrs)(in                                         Fixed Line
      INR/pulse)                                                                Plan
                                                                                Fixed Line
      STD Call Rate Fixed OffNet -                                              WLL Plan
      Video Call Rate (off Peak Hrs)(in
      INR/pulse)                                       STD Call Fixed OffNet -  Fixed Line
                                                       Validity in Days         Add On Pack
      STD Call Fixed OffNet -                                                   Prepaid STV
      Validity in Days
                                                                                Prepaid
                                                                                Combo

      CUP (Commercial Usage Policy), if  Alphanumeric  CUP for STD Call Rate Prepaid Plan
      any                                                                                  voucher

                                                                            P a g e 20 | 39

A123  Description of STD Call Rate / pulse  Alphanumeric  Description of STD Call
      rate in case any other pattern is                   Rate / pulse rate in case
A124  followed                                            any other pattern is       Prepaid STV
A125                                                      followed
A126                                                                                 Prepaid
A127                                                                                 Combo
A128
A129                                                                                 SUK
A130
A131                                                                                 Postpaid Plan
A132
A133                                                                                 Postpaid Add
A134                                                                                 On Pack

                                                                                     Fixed Line
                                                                                     Plan

                                                                                     Fixed Line
                                                                                     WLL Plan

      SMS Rate (in INR/SMS) -               Numeric       Parameters for SMS         Fixed Line
      All Local (onnet +Offnet)             Numeric       Rate                       Add On Pack
                                            Numeric                                  Prepaid Plan
      SMS Rate (in INR/SMS) -               Numeric                                  voucher
      All National (onnet +Offnet)          Numeric
                                            Numeric                                  Prepaid STV
      SMS Rate (in INR/SMS) -               Numeric
      Local Onnet                           Alphanumeric                             Prepaid
                                                                                     Combo
      SMS Rate (in INR/SMS) -
      Local Offnet                                                                   SUK

      SMS Rate (in INR/SMS) -                                                        Postpaid Plan
      National Onnet
                                                                                     Postpaid Add
      SMS Rate (in INR/SMS) -                                                        On Pack
      National Offnet
                                                                                     Fixed Line
      SMS Rate (in INR/SMS) -                                                        Plan
      International                                                                  Fixed Line
                                                                                     WLL Plan
      SMS Rate (in INR/SMS) - Terms
                                                          Terms and conditions       Fixed Line
      SMS Rate (in INR/SMS) - Validity      Numeric       including conditions       Add On Pack
                                                          pertaining to SMS Rate,
                                                          if any                     Prepaid STV
                                                          Validity (In Days)

                                                                                     Prepaid
                                                                                     Combo

      CUP (Commercial Usage Policy), if     Alphanumeric  CUP for SMS Rate           Prepaid Plan
      any                                   Alphanumeric                             voucher
      Description of SMS Rate, in case                    Description of SMS
      any other pattern is followed                       Rate, in case any other    Prepaid STV
                                                          pattern is followed
                                                                                     Prepaid
                                                                                     Combo

                                                                                     SUK

                                                                                     Postpaid Plan

                                                                                     Postpaid Add
                                                                                     On Pack

                                                                              P a g e 21 | 39

                                                                                     Fixed Line
                                                                                     Plan

                                                                                     Fixed Line
                                                                                     WLL Plan

A135  ISD call– ISD Countries (Country      Alphanumeric  Parameters for ISD Call    Fixed Line
A136  names separated by ‘,’)               Numeric       Rate                       Add On Pack
A137                                                                                 Prepaid STV
      ISD call -Pulse Rate (in seconds)
A138                                                                                 Prepaid
                                                                                     Combo
A139
      ISD Call Rate -ISD Calls to Mobile(in Numeric                                  Postpaid Add
A140  INR/pulse)                                                                     On Pack

A141                                                                                 Fixed Line
A142                                                                                 Add On Pack
A143
A144  ISD Call Rate -ISD calls to           Numeric
      Landline(in INR/pulse)
                                                                                     Gen ISD Tariff

      ISD Call Rate -ISD Video calls(in     Numeric
      INR/pulse)

      ISD Call Rate -Weblink for ISD Call Alphanumeric    Weblink for ISD call rate
      Rate                                                is compulsory if ISD
                                                          rates are applicable

      ISD Call Rate -Conditions, if any     Alphanumeric                             Prepaid
      ISD call -Validity (In Days)          Numeric                                  Combo

      CUP (Commercial Usage Policy), if     Alphanumeric  CUP for ISD Call Rate Prepaid STV
      any                                   Alphanumeric
                                                          Description of ISD Call    Prepaid
      Description of ISD Call Rate / pulse                Rate / pulse rate in case  Combo
      rate in case any other pattern is                   any other pattern is
      followed                                            followed                   Postpaid Add
                                                                                     On Pack

                                                                                     Fixed Line
                                                                                     Add On Pack

                                                                                     Gen ISD Tariff

A145  Call while Roaming - Pulse (in        Numeric       Parameters for Call        Prepaid Plan
A146  seconds)                                            Rate while roaming         voucher
A147
A148  Call Rate while Roaming – Incoming Numeric          Ceiling of Re. 0.80 per    Prepaid STV
      voice (in INR/pulse)                                minute for outgoing
                                                          local voice call while on  Prepaid
                                                          national roaming           Combo

      Call Rate while Roaming - Incoming Numeric          Ceiling of Re. 1.15 per    SUK
      video (in INR/pulse)                                minute for outgoing
                                                          STD voice call while on    Postpaid Plan
      Call Rate while Roaming - Local       Numeric       national roaming
      Outgoing                                                                       Postpaid Add
      voice (in INR/pulse)                                Ceiling of Re. 0.45 per    On Pack
                                                          minute for incoming
                                                          voice call while on

                                                                               P a g e 22 | 39

A149  Call Rate while Roaming – Local       Numeric       national roaming
A150  Outgoing
A151  video (in INR/pulse)
A152
A153  Call Rate while Roaming – STD         Numeric
      Outgoing
A154  voice (in INR/pulse)
A155
      Call Rate while Roaming – STD         Numeric                                 Prepaid STV
      Outgoing video (in INR/pulse)         Numeric

      Call while Roaming – Validity in
      Days

      Call Rate while Roaming -             Alphanumeric                            Prepaid
      Web link for National outgoing ISD                                            Combo
      Call Rate                                                                     Prepaid Plan
                                                                                    voucher

                                                                                    Prepaid STV

                                                                                    Prepaid
                                                                                    Combo

                                                                                    SUK

                                                                                    Postpaid Plan

      CUP (Commercial Usage Policy), if     Alphanumeric  CUP for Call Rate while   Postpaid Add
      any                                                 roaming                   On Pack
                                                                                    Prepaid Plan
                                                                                    voucher

      Description of Call Rate while        Alphanumeric  Description of Call Rate  Prepaid STV
      roaming in case any other pattern is                while roaming in case
      followed                                            any other pattern is      Prepaid
                                                          followed                  Combo

                                                                                    SUK

                                                                                    Postpaid Plan

                                                                                    Postpaid Add
                                                                                    On Pack

A156  SMS Rate while Roaming -              Numeric       Parameters for SMS        Prepaid Plan
      Local                                 Numeric       Rate while roaming        voucher
      in INR/SMS                            Numeric
                                                          Ceiling of Re. 0.25 per   Prepaid STV
A157  SMS Rate while Roaming -                            SMS for outgoing local
      National                                            SMS while on national     Prepaid
      in INR/SMS                                          roaming                   Combo

                                                          Parameters for SMS        SUK
                                                          Rate while roaming
                                                          CUP for SMS Rate          Postpaid Plan
                                                          while roaming
                                                                                    Postpaid Add
                                                          Ceiling of Re. 0.38 per   On Pack
                                                          SMS for outgoing STD
A158  SMS Rate while Roaming-                             SMS while on national
      International

                                                                            P a g e 23 | 39

      in INR/SMS                                           roaming

A159  SMS Rate while Roaming-                Numeric
      Any other ( please specify)
A160
      SMS while Roaming- Validity in days Numeric                                  Prepaid STV
A161
A162  CUP (Commercial Usage Policy), if      Alphanumeric  Description of SMS      Prepaid
      any                                    Alphanumeric  Rate while roaming in   Combo
      Description of SMS Rate / pulse rate                 case any other pattern  Prepaid Plan
      in case any other pattern is followed                is followed             voucher

                                                                                   Prepaid STV

                                                                                   Prepaid
                                                                                   Combo

                                                                                   SUK

                                                                                   Postpaid Plan

                                                                                   Postpaid Add
                                                                                   On Pack

A163  While International Roaming -          Alphanumeric  Parameters for charges  Prepaid STV
A164  ISD Countries (Country names                         while international
A165  separated by ‘,’)                                    roaming                 Prepaid
A166                                                                               Combo
A167  While International Roaming -          Numeric       Parameters for charges
A168  ISD Incoming Pulse (in seconds)                      while international     Postpaid Add
A169                                                       roaming                 On Pack
A170  Rate while International Roaming -     Numeric       CUP for SMS Rate
A171  ISD Incoming Calls                                   while roaming           International
A172                                                                               Roaming
A173
      While International Roaming -          Numeric
      ISD PulseOutgoing Local Calls (in
      seconds)

      Rate while International Roaming -     Numeric

      While International Roaming -          Numeric
      ISD PulseOutgoing Calls to India (in
      seconds)

      Rate while International Roaming -     Numeric
      ISD Outgoing Calls to India

      While International Roaming -          Numeric
      ISD PulseOutgoing Calls to Other
      Countries (in seconds)

      Rate while International Roaming -     Numeric
      ISD Outgoing Calls to Other
      Countries

      While International Roaming -ISD       Numeric
      Video call (in seconds)

      Rate while International Roaming -     Numeric
      ISD Outgoing SMS

                                                                    P a g e 24 | 39

A174  Rate while International Roaming -          Numeric
A175  ISD Incoming SMS
A176
A177  While International Roaming -               Numeric
A178  ISD PulseIncoming Free Usage (in
A179  seconds)
A180
A181  While International Roaming -               Numeric
A182  ISD Incoming Free Usage (in
A183  minutes)
A184
      While International Roaming -               Numeric
A185  ISD PulseOutgoing Free Usage (in
      seconds)
A186
      While International Roaming -               Numeric
A187  ISD Outgoing Free Usage (in
A188  minutes)
A189
      While International Roaming -               Alphanumeric
      ISD UnitFree Data Usage

      While International Roaming -               Numeric
      ISD Free Data Usage

      While International Roaming -               Numeric
      ISD Free SMS

      While International Roaming -               Numeric
      Validity (In Days)

      CUP (Commercial Usage Policy), if           Alphanumeric  Description of Ratewhile
      any                                         Alphanumeric  International Roaming
      Description of Ratewhile                                  in case any other
      International Roaming in case any           Alphanumeric  pattern is followed
      other pattern is followed (Should
      contain at least the weblink of the                       (J) Data Rate (Please     Prepaid STV
      tariff product in order to list it in TRAI                specify rate in paisa/
      consumer view.)                                           quantum of data           Prepaid
      Data Rate – Home                                          transfer e.g 2 paisa /    Combo
                                                                10KB )
      Data Rate - Roaming                         Alphanumeric                            Postpaid Add
                                                                (J) Data Rate (Please     On Pack
                                                                specify rate in paisa/
                                                                quantum of data           International
                                                                transfer e.g 2 paisa /    Roaming
                                                                10KB )

      Data Rate - Conditions                      Alphanumeric  Conditions pertaining to
                                                                data rate , if any

      Monthly Rental for International            Numeric       Monthly rental Charges    Prepaid STV
      roaming (in Rs.)                                          while
                                                                RoamingInternational      Prepaid
      Weblink for Rates while international Alphanumeric                                  Combo
      roaming                                                   Weblink for Rates while
                                                                international roaming     Postpaid Plan

                                                                This field is compulsory  Postpaid Add
                                                                if ISD roaming rates are  On Pack
                                                                applicable
                                                                                          International
                                                                                          Roaming

                                                                                        P a g e 25 | 39

A190  Duration for Additional Benefits-Time Alphanumeric  If applicable, additional   Prepaid Plan
A191  From (hh:mm:ss)                                     benefits start time to be   voucher
A192                                                      specified in hh:mm:ss
A193  Duration for Additional Benefits-Time Alphanumeric  If applicable, additional   Prepaid STV
A194  Till (hh:mm:ss)                                     benefits till - time to be
A195                                                      specified in hh:mm:ss       Prepaid
A196  Additional Local(in minutes) -      Numeric         Parameters for              Combo
A197  Local (in minutes)                                  Additional Benefits –
A198                                                      Additional Local            SUK
A199
      Additional Local(in minutes) -      Numeric         Parameters for              Postpaid Plan
A200  Local Onnet(in minutes)                             Additional Benefits –
A201                                                      Additional Local            Postpaid Add
                                                                                      On Pack

      Additional Local(in minutes) -      Numeric                                     Fixed Line
      Local Offnet(in minutes)                                                        Plan
                                                                                      Fixed Line
      Additional Local(in minutes) -      Numeric                                     WLL Plan
      Local Mobile(in minutes)
                                                                                      Fixed Line
                                                                                      Add On Pack

      Additional Local(in minutes) -      Numeric
      Local Onnet Mobile(in minutes)      Numeric

      Additional Local(in minutes) -
      Local Offnet Mobile(in minutes)

      Additional Local(in minutes) -      Numeric                                     Prepaid STV
      Validity (In Days)                  Alphanumeric
      Description of Additional Local in                  Description of Additional   Prepaid
      case any other pattern is followed  Numeric         Local in case any other     Combo
                                          Numeric         pattern is followed         Prepaid Plan
      Additional STD(in minutes) -                                                    voucher
      Local (in minutes)
      Additional STD(in minutes) -                                                    Prepaid STV
      Local Onnet(in minutes)
                                                                                      Prepaid
                                                                                      Combo

                                                                                      SUK

                                                                                      Postpaid Plan

                                                                                      Postpaid Add
                                                                                      On Pack

                                                                                      Fixed Line
                                                                                      Plan

                                                                                      Fixed Line
                                                                                      WLL Plan

                                                                                      Fixed Line
                                                                                      Add On Pack

                                                          Parameters for              Prepaid Plan
                                                          Additional Benefits –       voucher
                                                          Additional STD
                                                                                      Prepaid STV

                                                                                      Prepaid
                                                                                      Combo

                                                                                 P a g e 26 | 39

A202  Additional STD(in minutes) -          Numeric                                  SUK
A203  Local Offnet(in minutes)              Numeric
A204                                        Numeric                                  Postpaid Plan
A205  Additional STD(in minutes) -          Numeric
A206  Local Mobile(in minutes)                                                       Postpaid Add
A207                                                                                 On Pack
      Additional STD(in minutes) -
A208  Local Onnet Mobile(in minutes)                                                 Fixed Line
A209                                                                                 Plan
A210  Additional STD(in minutes) -
A211  Local Offnet Mobile(in minutes)                                                Fixed Line
A212                                                                                 WLL Plan
A213
                                                                                     Fixed Line
                                                                                     Add On Pack

      Additional STD(in minutes) -          Numeric                                  Prepaid STV
      Validity (In Days)

                                                                                     Prepaid
                                                                                     Combo

      Description of Additional STD in      Alphanumeric  Description of Additional  Prepaid Plan
      case any other pattern is followed                  STD in case any other      voucher
                                                          pattern is followed
                                                                                     Prepaid STV

                                                                                     Prepaid
                                                                                     Combo

                                                                                     SUK

                                                                                     Postpaid Plan

                                                                                     Postpaid Add
                                                                                     On Pack

                                                                                     Fixed Line
                                                                                     Plan
                                                                                     Fixed Line
                                                                                     WLL Plan

                                                                                     Fixed Line
                                                                                     Add On Pack

      Additional Local & STD(in minutes) - Numeric        Parameters for             Prepaid Plan
      Local & STD (in minutes)                            Additional Benefits –      voucher
                                                          Additional Local & STD
                                                                                     Prepaid STV

      Additional Local & STD(in minutes) - Numeric                                   Prepaid
      Local & STD Onnet (in minutes)                                                 Combo

      Additional Local & STD(in minutes) - Numeric                                   SUK
      Local & STD Offnet (in minutes)
                                                                                     Postpaid Plan
      Additional Local & STD(in minutes) - Numeric
      Local & STD Mobile (in minutes)                                                Postpaid Add
                                                                                     On Pack

      Additional Local & STD(in minutes) -  Numeric                                  Fixed Line
      Local & STD Onnet Mobile (in                                                   Plan
      minutes)                                                                       Fixed Line
                                                                                     WLL Plan

      Additional Local & STD(in minutes) - Numeric                                   Fixed Line
      Local & STD Offnet Mobile (in                                                  Add On Pack

                                                          P a g e 27 | 39

      minutes)

A214  Additional Local & STD(in minutes) - Numeric                                  Prepaid STV
A215  Validity (In Days)

A216  Description of Additional Local &   Alphanumeric   Description of Additional  Prepaid
A217  STD in case any other pattern is                   Local & STD in case        Combo
A218  followed                                           any other pattern is       Prepaid Plan
A219                                                     followed                   voucher

                                                                                    Prepaid STV

                                                                                    Prepaid
                                                                                    Combo

                                                                                    SUK

                                                                                    Postpaid Plan

                                                                                    Postpaid Add
                                                                                    On Pack

                                                                                    Fixed Line
                                                                                    Plan
                                                                                    Fixed Line
                                                                                    WLL Plan

                                                                                    Fixed Line
                                                                                    Add On Pack

      Additional Local, STD & Roaming(in  Numeric        Parameters for             Prepaid Plan
      minutes) -                                         Additional Benefits –      voucher
      Local, STD & Roaming (in minutes)                  Additional Local, STD &
                                                         Roaming                    Prepaid STV

      Additional Local, STD & Roaming(in  Numeric                                   Prepaid
      minutes) -                                                                    Combo
      Local, STD & Roaming Mobile (in
      minutes)                                                                      SUK

                                                                                    Postpaid Plan

                                                                                    Postpaid Add
                                                                                    On Pack

      Additional Local, STD & Roaming(in  Numeric                                   Prepaid STV
      minutes) -
      Validity (In Days)                                                            Prepaid
                                                                                    Combo

      Description of Additional Local, STD Alphanumeric  Description of Additional  Prepaid Plan
      & Roaming in case any other pattern                Local, STD & Roaming       voucher
      is followed                                        in case any other
                                                         pattern is followed        Prepaid STV

                                                                                    Prepaid
                                                                                    Combo

                                                                                    SUK

                                                                                    Postpaid Plan

                                                                                    Postpaid Add
                                                                                    On Pack

                                                         P a g e 28 | 39

A220  Additional Roaming(in minutes) -  Numeric          Parameters for             Prepaid Plan
A221  Incoming & Outgoing (in minutes)                   Additional Benefits –      voucher
A222                                                     Additional Roaming
A223                                                                                Prepaid STV
A224  Additional Roaming(in minutes) -  Numeric
A225  Incoming Free (in minutes)                                                    Prepaid
A226                                                                                Combo
A227  Additional Roaming(in minutes) -  Numeric
      Outgoing Free (in minutes)                                                    SUK
A228
A229  Additional Roaming(in minutes) -  Numeric                                     Postpaid Plan
A230  Outgoing Local & STD Mobile
A231  Free(in minutes)                                                              Postpaid Add
A232                                                                                On Pack
A233
      Additional Roaming(in minutes) -  Numeric
      Outgoing Local Free (in minutes)

      Additional Roaming(in minutes) -  Numeric
      Outgoing STD Free (in minutes)

      Additional Roaming(in minutes) -  Numeric                                     Prepaid STV
      Validity (In Days)

      Description of Additional Roaming in Alphanumeric  Description of Additional  Prepaid
      case any other pattern is followed                 Roaming in case any        Combo
                                                         other pattern is followed  Prepaid Plan
                                                                                    voucher

                                                                                    Prepaid STV

                                                                                    Prepaid
                                                                                    Combo

                                                                                    SUK

                                                                                    Postpaid Plan

      Additional SMS -                  Numeric          Parameters for             Postpaid Add
      Local & National                  Numeric          Additional Benefits –      On Pack
                                        Numeric          Additional SMS             Prepaid Plan
      Additional SMS -                  Numeric                                     voucher
      Local & National Onnet            Numeric
                                        Numeric                                     Prepaid STV
      Additional SMS -
      Local & National Offnet                                                       Prepaid
                                                                                    Combo
      Additional SMS -
      Local                                                                         SUK

      Additional SMS -                                                              Postpaid Plan
      Local Onnet
      Additional SMS -                                                              Postpaid Add
      Local Offnet                                                                  On Pack

                                                                                    Fixed Line
                                                                                    Plan
                                                                                    Fixed Line
                                                                                    WLL Plan

                                                                                    Fixed Line

                                                                                P a g e 29 | 39

                                                                                   Add On Pack

A234  Additional SMS -                    Numeric
A235  National                            Numeric
A236
A237  Additional SMS -
A238  National Onnet
A239
      Additional SMS -                    Numeric
A240  National Offnet                     Numeric
A241
      Additional SMS -
A242  International

      Additional SMS -                    Numeric                                  Prepaid STV
      Validity (In Days)                  Alphanumeric
      Description of Additional SMS in                  Description of Additional  Prepaid
      case any other pattern is followed  Alphanumeric  SMS in case any other      Combo
                                          Alphanumeric  pattern is followed        Prepaid Plan
      Additional ISD -                                                             voucher
      Summary of ISD freebies             Numeric
      Additional ISD -                                                             Prepaid STV
      Weblink for ISD freebies
                                                                                   Prepaid
      Additional ISD -                                                             Combo
      Validity (In Days)
                                                                                   SUK

                                                                                   Postpaid Plan

                                                                                   Postpaid Add
                                                                                   On Pack

                                                                                   Fixed Line
                                                                                   Plan

                                                                                   Fixed Line
                                                                                   WLL Plan

                                                        Parameters for             Fixed Line
                                                        Additional Benefits –      Add On Pack
                                                        Additional ISD             Prepaid Plan
                                                                                   voucher

                                                                                   Prepaid STV

                                                                                   Prepaid
                                                                                   Combo

                                                                                   Postpaid Plan

                                                                                   Postpaid Add
                                                                                   On Pack

                                                                                   Fixed Line
                                                                                   Plan
                                                                                   Fixed Line
                                                                                   WLL Plan

                                                                                   Fixed Line
                                                                                   Add On Pack

                                                                                   Prepaid STV

                                                                                   Prepaid

                                                                               P a g e 30 | 39

A243  Description of Additional ISD in case Alphanumeric  Description of Additional  Combo
      any other pattern is followed                       ISD in case any other      Prepaid Plan
A244                                                      pattern is followed        voucher
A245
A246                                                                                 Prepaid STV
A247
A248                                                                                 Prepaid
A249                                                                                 Combo
A250
A251                                                                                 Postpaid Plan
A252
                                                                                     Postpaid Add
                                                                                     On Pack

                                                                                     Fixed Line
                                                                                     Plan
                                                                                     Fixed Line
                                                                                     WLL Plan

      Additional Video Call -  Numeric                    Parameters for             Fixed Line
      Local & STD Video        Numeric                    Additional Benefits –      Add On Pack
                               Numeric                    Additional Video Call
      Additional Video Call -  Numeric                                               Prepaid Plan
      Local Video              Numeric                                               voucher

      Additional Video Call -                                                        Prepaid STV
      Local Video Onnet
                                                                                     Prepaid
      Additional Video Call -                                                        Combo
      Local Video Offnet
                                                                                     SUK
      Additional Video Call -
      STD Video                                                                      Postpaid Plan

                                                                                     Postpaid Add
                                                                                     On Pack

      Additional Video Call -  Numeric
      STD Video Onnet

      Additional Video Call -  Numeric                                               Prepaid STV
      STD Video Offnet         Numeric

      Additional Video Call -
      Validity (In Days)

                                                                                     Prepaid
                                                                                     Combo

      Description of Additional Video Call Alphanumeric   Description of Additional  Prepaid Plan
      in case any other pattern is followed               Video Call in case any     voucher
                                                          other pattern is followed
                                                                                     Prepaid STV

                                                                                     Prepaid
                                                                                     Combo

                                                                                     SUK

                                                                                     Postpaid Plan

                                                                                     Postpaid Add

                                                                                 P a g e 31 | 39

                                                                                   On Pack

A253  Additional Data -                   Alphanumeric  Parameters for             Prepaid Plan
A254  Unit (MB / GB)                      Numeric       Additional Benefits –      voucher
A255                                      Numeric       Additional Data
A256  Additional Data -                   Numeric                                  Prepaid STV
A257  Total 2G Data                       Numeric
A258  Additional Data -                   Numeric                                  Prepaid
A259  Total 3G Data                       Numeric                                  Combo
A260                                      Numeric
A261  Additional Data -                   Alphanumeric                             SUK
A262  Total 4G Data                       Numeric
A263                                      Alphanumeric                             Postpaid Plan
A264  Total Data (For ISP / Fixed Line    Alphanumeric
A265  Tariff / Fixed Line Add On Pack)    Alphanumeric                             Postpaid Add
      Additional Data -                                                            On Pack
A266  Day/Night Data Capping              Alphanumeric
A267                                      Alphanumeric                             Fixed Line
      Additional Data -                                                            Plan
      Weekly Data Capping                                                          Fixed Line
                                                                                   WLL Plan
      Additional Data -
      Monthly Data Capping                                                         Fixed Line
                                                                                   Add On Pack
      Additional Data -
      Carry Forward (Yes / No)                                                     ISP
                                                                                   Prepaid Plan
      Additional Data -                                                            voucher
      Validity (In Days)
                                                                                   Prepaid STV
      Additional Data -
      FUP, if any (Yes/No)                                                         Prepaid
                                                                                   Combo
      Additional Data -
      Condition, if any                                                            Prepaid Top
                                                                                   Up
      Description of Additional Data in
      case any other pattern is followed                                           Prepaid VAS

      Miscellaneous -                                                              Promo Offer
      Special benefits , if any
                                                                                   SUK
      Miscellaneous -
      Other charges, if any                                                        Postpaid Plan

                                                                                   Postpaid Add
                                                                                   On Pack

                                                        Description of Additional  Postpaid VAS
                                                        Data in case any other
                                                        pattern is followed        Fixed Line
                                                                                   Plan

                                                                                   Fixed Line
                                                                                   WLL Plan

                                                                                   Fixed Line
                                                                                   Add On Pack

                                                        Parameters for             ISP
                                                        Miscellaneous
                                                                                   Prepaid Plan
                                                                                   voucher

                                                                                   Prepaid STV

                                                                               P a g e 32 | 39

A268  Miscellaneous -                       Alphanumeric                             Prepaid
A269  Remarks, if any                                                                Combo
A270
A271  Miscellaneous -                       Alphanumeric                             Prepaid Top
A272  Terms and Conditions,if any                                                    Up
A273
A274  Miscellaneous -                       Alphanumeric                             Prepaid VAS
A275  Mode of Activation / Recharge
A276  (Website / App only / paper / USSD /                                           Promo Offer
      3rd party Wallet etc)
A277                                                                                 SUK
      Miscellaneous -                       Alphanumeric
A278  Whether details of this service have                                           Postpaid Plan
      been uploaded on the website
      (Either “Yes” or “No” should be                                                Postpaid Add
      entered)                                                                       On Pack

      Miscellaneous -                       Alphanumeric                             Postpaid VAS
      TSP website link of the Plan
                                                                                     Fixed Line
      Miscellaneous -                       Alphanumeric                             Plan
      Any other declarations
                                                                                     Fixed Line
      Miscellaneous -                       Alphanumeric                             WLL Plan
      Condition for termination of Product
      if any                                                                         Fixed Line
                                                                                     Add On Pack

                                                                                     ISP

      Miscellaneous -                       Alphanumeric                             Prepaid STV
      Activation Code If Any                Alphanumeric
                                                                                     Prepaid
      Miscellaneous -                                                                Combo
      Deactivation Code If Any
                                                                                     Prepaid VAS

                                                                                     Promo Offer

                                                                                     Postpaid Add
                                                                                     On Pack

      Delayed Submission (‘Yes’ or ‘No’) Alphanumeric     For timely submission,     Postpaid VAS
                                                          ‘No’ should be entered.    All Tariff
                                                          If it is a delayed tariff  Product Types
                                                          product submission,
                                                          ‘Yes’ should be entered

      Reason for delay                      Alphanumeric  This is a compulsory       All Tariff
                                                          field.                     Product Types

                                                          If it is a delayed
                                                          submission, the reason
                                                          for delay should be
                                                          entered here. If not a
                                                          delayed submission,
                                                          ‘Nil’ should be entered
                                                          in this field.

                                                          This is a compulsory
                                                          field.

                                                                                P a g e 33 | 39

Annexure 2

Format of Unique Record ID No.

The ‘Unique Record ID No.’ field for each tariff product should be a 12 digit unique
alphanumeric ID, which should follow the following format :

    1. The first two alphabets should be the TSP code, as per Annexure 3
    2. The next two alphabets should be the LSA code, as per Annexure 4
    3. The next fouralphabets should be the Tariff Product Code, as per Annexure 2
    4. The last 4 digits should be numbers.

List of Tariff Product Types  Tariff Product Code
                              PMPV
Tariff Product Type           PMST
Prepaid Plan Voucher          PMCM
Prepaid STV                   PMTP
Prepaid Combo                 PMVS
Prepaid Top Up                PMPO
Prepaid VAS
Prepaid Promo Offer

                                                   P a g e 34 | 39

SUK                              PMSK
Postpaid Plan                    OMPL
Postpaid Add On Pack             OMPA
Postpaid VAS                     OMVS
Postpaid Promo Offer             OMPO
Postpaid Fixed Line Plan         OFLP
Prepaid Fixed Line Plan          PFLP
Prepaid Fixed Line Add On Pack   PFLA
Postpaid Fixed Line Add On Pack  OFLA
Postpaid Fixed Line WLL Plan     OFWL
Prepaid Fixed Line WLL Plan      PFWL
Prepaid Gen ISD Tariff           PMGI
Postpaid Gen ISD Tariff          OMGI
Prepaid ISP                      PISP
Postpaid ISP                     OISP

                                       P a g e 35 | 39

P a g e 36 | 39

Annexure 3
Format of Unique Record ID No.

The ‘Unique Record ID No.’ field for each tariff product should be a 12 digit unique
alphanumeric ID, which should follow the following format :

    1. The first two alphabets should be the TSP code, as per Annexure 3
    2. The next two alphabets should be the LSA code, as per Annexure 4
    3. The next four alphabets should be the Tariff Product Code, as per Annexure 2
    4. The last 4 digits should be numbers.

TSP Names as registered in the Database  TSP Code
TSP Names                                AC
Aircel                                   AT
Airtel                                   BS
BSNL                                     ID
Idea                                     JI
Jio                                      MT
MTNL                                     QD
Quadrant (Connect)                       TT
Tata Tele                                TL
Telenor                                  VD
Vodafone

                                                   P a g e 37 | 39

Annexure 4
Format of Unique Record ID No.

The ‘Unique Record ID No.’ field for each tariff product should be a 12 digit unique
alphanumeric ID, which should follow the following format :

    1. The first two alphabets should be the TSP code, as per Annexure 3
    2. The next two alphabets should be the LSA code, as per Annexure 4
    3. The next four alphabets should be the Tariff Product Code, as per Annexure 2
    4. The last 4 digits should be numbers.

LSA Names as registered in the Database  LSA Code
LSA Names

All India                                01

Andhra Pradesh                           02

Assam                                    03

Bihar                                    04

Chennai and Tamil Nadu                   05

Delhi                                    06

Gujarat                                  07

Haryana                                  08

Himachal Pradesh                         09

Jammu and Kashmir                        10

Karnataka                                11

Kerala                                   12

Kolkata                                  13

Madhya Pradesh                           14

Maharashtra                              15

Mumbai                                   16

North East                               17

Odisha                                   18

Punjab                                   19

Rajasthan                                20

UP East                                  21

UP West                                  22

West Bengal                              23

                                                   P a g e 38 | 39

P a g e 39 | 39
