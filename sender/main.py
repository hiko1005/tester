from SiteService import SiteService
from CheckService import CheckService
from Reporter import Reporter


def main():
    with SiteService() as s:
        sites = s.get_active()
        sites = CheckService().check(sites)
        s.update_status(sites)
        Reporter().report(sites[0])

if __name__ == "__main__":
    main()
