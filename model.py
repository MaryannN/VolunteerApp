# Dictionaries 
# maybe another dictionary/list element for link name so it doesnt all just say "bronx zoo" or whatev we hard code - DONE
# Very helpful when builing - https://www.volunteermatch.org/

x = {
  "Baychester": {
    "Environmental": ["http://www.greencitychallenge.org/", "Green City Challenge"],
    "Animal": ["https://www.nycatcoal.org/", "New York City Cat Coalition"],
    "Social": ["https://www.nycservice.org/organizations/157", "Baychester Youth Council"],
	  "Healthcare": ["https://afyafoundation.org/", "Afya Foundation of America"]
  },
  "Morris Park": {
    "Environmental": ["https://bronxzoo.com/volunteering/discovery-guide-volunteer-program", "Discovery Guide Volunteer Program - Bronx Zoo"],
    "Animal": ["https://www.facebook.com/astoriacatrescue/", "Astoria Cat Rescue"],
    "Social": ["https://southbronxunited.org/", "South Bronx United"],
	  "Healthcare": ["http://www.littlesistersfamily.org/", "LSA Family Health Service"]
  },
  "Fordham": {
    "Environmental": ["https://www.bronxisblooming.org/", "Bronx is Blooming"],
    "Animal": ["https://www.searchandcare.org/", "Search and Care"],
    "Social": ["https://potsbronx.org/english/", "POTS Bronx"],
	  "Healthcare": ["http://www.mandalacafe.org/", "Mandala Cafe"]
  },
  "Riverdale": {
    "Environmental": ["https://bronxriver.org/", "Bronx River Alliance"],
    "Animal": ["https://www.heartsandbonesrescue.com/", "Hearts & Bones Rescue"],
    "Social": ["https://www.riverdaley.org/programs/volunteer/#overview", "Riverdale Y"],
	  "Healthcare": ["https://locations.amedisys.com/nj/hackensack/amedisys-hospice-care.html", "Amedisys Hospice Services"]
  }
}

def volunteer(choice1, choice2):
  return x[choice1][choice2]
