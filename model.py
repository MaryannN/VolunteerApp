# Dictionaries 
# maybe another dictionary/list element for link name so it doesnt all just say "bronx zoo" or whatev we hard code - DONE
# Very helpful when builing - https://www.volunteermatch.org/

x = {
  "Baychester": {
    "Environmental": ["http://www.greencitychallenge.org/", "Green City Challenge", "The mission of Green City Challenge is to educate people in New York City and beyond about ways to live, work and eat green."],
    "Animal": ["https://www.nycatcoal.org/", "New York City Cat Coalition", "We rescue cats and kittens from the streets and outdoors, or from owner surrender, bring them for needed veterinary services, give them love, and find them loving forever homes! We are a 100% Zero Kill rescue, 100% volunteer-based, 501(C)(3) non-profit, grassroots organization. When you adopt a cat from us, it will create a space for us to rescue another cat! Thank you for considering our organization."],
    "Social": ["https://www.nycservice.org/organizations/157", "Baychester Youth Council", "BYC's current program includes six essential components: education (e.g., after-school programs, holiday and summer camp programs, youth apprenticeships, college preparation and enrollment, and leadership and computer training); health referral services (e.g., medical referral, testing and prevention services); human service referrals (e.g., legal, counseling and social services); creative arts programs; recreational opportunities; and parental, school and community involvement in the success of our programs."],
	  "Healthcare": ["https://afyafoundation.org/", "Afya Foundation of America", "The mission of the Afya Foundation is to recover targeted surplus medical supplies, hospital equipment and humanitarian provisions from the New York healthcare, corporate and private communities in order to establish categorized inventory to support ongoing health initiatives in Africa and the Caribbean."]
  },
  
  "Morris Park": {
    "Environmental": ["https://bronxzoo.com/volunteering/discovery-guide-volunteer-program", "Discovery Guide Volunteer Program - Bronx Zoo", "As a Discovery Guide, you will educate visitors about the animals in our zoos and how we care for them through fun and engaging activities. You will also share stories about our conservation programs and inspire children and adults to take actions that benefit wildlife and the environment. You may also assist with a variety of education programs."],
    "Animal": ["https://www.facebook.com/astoriacatrescue/", "Astoria Cat Rescue", "Astoria Cat Rescue is a non-profit 501(c)(3) organization. Please join our Kitty Crew to help support the 100+ homeless cats we rescue and feed every day in Astoria and Long Island City (LIC) in Queens, New York! Volunteer, foster, adopt, or donate!"],
    "Social": ["https://southbronxunited.org/", "South Bronx United", "South Bronx United is a youth development organization dedicated on serving the South Bronx through education, mentoring, and soccer programs. Our goal is use the sport and the strength of mentoring to help boys and girls, ages 4-19, develop as leaders and scholars."],
	  "Healthcare": ["http://www.littlesistersfamily.org/", "LSA Family Health Service", "LSA Family Health Service, founded by the Little Sisters of the Assumption, strengthens and empowers vulnerable families and children by meeting their basic needs for food, healthcare, education and a safe home, in the belief that affirming families in their own dignity improves the entire community."]
  },
  
  "Fordham": {
    "Environmental": ["https://www.bronxisblooming.org/", "Bronx is Blooming", "At The Bronx is Blooming (BiB), our mission is to grow and support a culture of environmental stewardship in the Bronx. BiB inspires communities to advocate for their parkland as well as promote civic engagement, youth development, and community building."],
    "Animal": ["https://www.searchandcare.org/", "Search and Care", "Search and Care is a not for profit social service agency that has helped over 10,000 residents ranging from the ages 60-108. Volunteers help us out tremendously. They go to our client’s homes and help make their day a bit easier. They will sit and listen to stories, read to those with deteriorating vision, food shop for those who cannot carry groceries up the stairs of their apartment. Our volunteers take our clients’ dogs for walks and also accompany our clients to doctor appointments or help run local errands."],
    "Social": ["https://potsbronx.org/english/", "POTS Bronx", "The mission of Part of the Solution (POTS) is to be a loving community in the Bronx that nourishes the basic needs and hungers of all who come to our door. Founded in 1982 as a soup kitchen, POTS has expanded its mission from feeding its neighbors to nourishing the myriad of needs of the community in a holistic way."],
	  "Healthcare": ["http://www.mandalacafe.org/", "Mandala Cafe", "We are committed to providing access, mutuality and dignity around issues of food."]
  },
  
  "Riverdale": {
    "Environmental": ["https://bronxriver.org/", "Bronx River Alliance", "The Bronx River Alliance serves as a coordinated voice for the river. We work in harmonious partnership to protect, improve and restore the Bronx River corridor. Our goal is to make a healthy ecological, recreational, educational, and economic resource for all communities through which the river flows."],
    "Animal": ["https://www.heartsandbonesrescue.com/", "Hearts & Bones Rescue", "Hearts & Bones Rescue is a 501(c)(3) non-profit organization composed of a network of fosters and volunteers who collaborate to rescue shelter dogs and find them loving, forever homes. Every day, there are thousands of animals killed in America's shelters because they do not have homes. As a foster-based rescue, we focus on providing all of our dogs with secure and caring environments while they wait for their forever families. At Hearts & Bones, all of our dogs are 100% certified pre-loved."],
    "Social": ["https://www.riverdaley.org/programs/volunteer/#overview", "Riverdale Y", "The Riverdale Y is a multi-generational agency providing informal education, leisure time activities, and social services to meet the recreational, social, and cultural needs of the Jewish and the general community."],
	  "Healthcare": ["https://locations.amedisys.com/nj/hackensack/amedisys-hospice-care.html", "Amedisys Hospice Services", "We’re here to provide physical, emotional, and spiritual care and support during a life-limiting illness, along with help for families and caregivers."]
  }
}

def volunteer(choice1, choice2):
  return x[choice1][choice2]
