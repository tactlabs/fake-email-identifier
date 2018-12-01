# emailid_finder Package
  This will find email-id is fake or not

##Installation

Run the following to install:

'''python

pip install fake-email-identifier
'''

##Usage

'''python
import emailid_finder as ef

#Generate "True"

ef.check('namubol@veanlo.com') //This id form https://temp-mail.org/en/

#Generate "False"

ef.check('<some real email>')
