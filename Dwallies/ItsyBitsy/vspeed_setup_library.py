from varspeed import Vspeed

#Opinionator
vs_outputopinion1 = Vspeed(init_position=0, result="int")
vs_outputopinion2 = Vspeed(init_position=0, result="int")
vs_outputopinion3 = Vspeed(init_position=0, result="int")
vs_outputopinion4 = Vspeed(init_position=0, result="int")


#emotional damage
vs_outputemo1 = Vspeed(init_position=0, result="int")
vs_outputemo2 = Vspeed(init_position=0, result="int")
vs_outputemo3 = Vspeed(init_position=0, result="int")
vs_outputemo4 = Vspeed(init_position=0, result="int")
vs_outputemo5 = Vspeed(init_position=0, result="int")

#forest
vs_outputforest1 = Vspeed(init_position=0, result="int")
vs_outputforest2 = Vspeed(init_position=0, result="int")

#animal abuse
vs_outputanimal = Vspeed(init_position=0, result="int")
vs_outputanimal1 = Vspeed(init_position=0, result="int")
vs_outputanimal2 = Vspeed(init_position=0, result="int")
vs_outputanimal3 = Vspeed(init_position=0, result="int")


#billip pheesley
vs_outputphillip1 = Vspeed(init_position=0, result="int")
vs_outputphillip2  = Vspeed(init_position=0, result="int")


#overig
vs_outputoverig1 = Vspeed(init_position=0, result="int")
vs_outputoverig2 = Vspeed(init_position=0, result="int")



def vspeed_setup():
    #Opinionator
    vs_outputopinion1.set_bounds(lower_bound=0, upper_bound=255)
    vs_outputopinion2.set_bounds(lower_bound=0, upper_bound=255)
    vs_outputopinion3.set_bounds(lower_bound=0, upper_bound=255)
    vs_outputopinion4.set_bounds(lower_bound=0, upper_bound=255)

    #emotional damage
    vs_outputemo1.set_bounds(lower_bound=0, upper_bound=255)
    vs_outputemo2.set_bounds(lower_bound=0, upper_bound=255)
    vs_outputemo3.set_bounds(lower_bound=0, upper_bound=255)
    vs_outputemo4.set_bounds(lower_bound=0, upper_bound=255)
    vs_outputemo5.set_bounds(lower_bound=0, upper_bound=255)

    #forest
    vs_outputforest1.set_bounds(lower_bound=0, upper_bound=255)
    vs_outputforest2.set_bounds(lower_bound=0, upper_bound=255)

    #animal abuse

    vs_outputanimal.set_bounds(lower_bound=0, upper_bound=255)
    vs_outputanimal1.set_bounds(lower_bound=0, upper_bound=255)
    vs_outputanimal2.set_bounds(lower_bound=0, upper_bound=255)
    vs_outputanimal3.set_bounds(lower_bound=0, upper_bound=255)

    #billip pheesley
    vs_outputphillip1 .set_bounds(lower_bound=0, upper_bound=255)
    vs_outputphillip2 .set_bounds(lower_bound=0, upper_bound=255)

    #overig
    vs_outputoverig1.set_bounds(lower_bound=0, upper_bound=255)
    vs_outputoverig2.set_bounds(lower_bound=0, upper_bound=255)
