"""
Robin is a data engineer and loves apples. His favourite type of apple is Fuji.
Apples are grown in Spain and in France which are countries in Europe.
Robin also likes to go ski and climb in France.
Robin is teaching a course on RDF in Zurich on the 12th of march
"""






Robin teaching <BedrettoCourse>
<BedrettoCourse> hasTopic <RDF>
<BedrettoCourse> hasDate "12.03.25"
<BedrettoCourse> hasLocation <Zurich>





Robin <likes> <skiing in France> 
robin <likes> climbing in france
robin <likes> climbing in italy
robin <likes> climbing in spain


climbing <subClassOf> <Sport>
Skiing <subClassOf> <Sport>

<climbing> canBeDoneIn <France>, <Italy>, <Spain>, <Morrocan desert>
<skiing> canBeDoneIn <France>, <Italy>, <Spain>

But wait!
climbing and skiing have something in common

<Sport> canBeDoneIn <country> 
hmmmm

skiing can only be done in countries that have snow AND mountains
climbing can only be done in countries that have mountains

What is this information going to be used for?!
