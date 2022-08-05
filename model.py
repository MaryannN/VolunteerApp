# Dictionaries 
# maybe another dictionary/list element for link name so it doesnt all just say "bronx zoo" or whatev we hard code

# x = {
#  "Morris Park": ["https://bronxzoo.com/volunteering/discovery-guide-volunteer-program", ""] 
#   "Baychester": ["https://www.nycservice.org/organizations/157", ""], 
#   "Morris Park": ["https://bronxzoo.com/volunteering/discovery-guide-volunteer-program", ""], 
#   "Fordham": ["https://potsbronx.org/english/", "https://www.bronxisblooming.org/"],
#   "Riverdale": ["https://www.riverdaley.org/programs/volunteer/#overview", ""]
# }

x = {
  "Baychester": {
  #[
  #   "https://bronxzoo.com/volunteering/discovery-guide-volunteer-program", "https://www.aspca.org/", "https://www.nycservice.org/organizations/157", "https://www.healthcare.gov/"
  # ]
    "Environmental": "https://bronxzoo.com/volunteering/discovery-guide-volunteer-program",
    "Animal": "https://www.aspca.org/",
    "Social": "https://www.nycservice.org/organizations/157",
	"Healthcare": "https://www.healthcare.gov/"
  },
  "Morris Park": {
    "Environmental" : "https://bronxzoo.com/volunteering/discovery-guide-volunteer-program",
    "Animal": "morris animal",
    "Social": "morris social",
	"Healthcare": "morris health"
  },
  "Fordham": {
    "Environmental" : "https://www.bronxisblooming.org/",
    "Animal": "fordham animal",
    "Social": "https://potsbronx.org/english/",
	"Healthcare": "fordham health"
  },
  "Riverdale": {
    "Environmental" : "riverdale environment",
    "Animal": "riverdale animal",
    "Social": "https://www.riverdaley.org/programs/volunteer/#overview",
	"Healthcare": "riverdale health"
  }
}

def volunteer(choice1, choice2):
  return x[choice1][choice2]
  
# Conditionals




