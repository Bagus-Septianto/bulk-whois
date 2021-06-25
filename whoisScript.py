import whois

domainList = open('domainListEx.txt', 'r')   # open domain lists from file

for domain in domainList:                    # looping each line and get single domain
    file = open('whois-report', 'a')         # open report file to append the report
    domain = domain.rstrip("\n")             # removing "enter" from the domain. so it will be whois-able
    try:
        res = whois.whois(domain, flags=0 | whois.NICClient.WHOIS_QUICK) # flags used to fix 'Error trying to connect to socket: closing socket' #60, also run faster
        expDate = res.expiration_date                                    # take the expiration date from whois response
        file.write(domain + '; ')                                        # write the domain name and adding '; ' to convert the file to csv easier

        try:
            for eachExpDate in expDate:              # if theres multiple exp date loop and take first one to write on report
                file.write(str(eachExpDate) + ';\n')
                break
        except:
            file.write(str(expDate) + ';\n')         # write the exp date if its just 1 exp date
        finally:
            file.close()
    except:
        file.write(domain + '; ' + 'Available;\n')   # if domain whois not found, write available
        file.close()
        pass