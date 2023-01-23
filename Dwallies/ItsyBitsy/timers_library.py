from timer import Timer
#timers

forest_timer = Timer()
forest_timer_on = False

emotional_damage_timer = Timer()
emotional_damage_timer_on = False

overig_timer = Timer()
overig_timer_on = False

animal_timer = Timer()
animal_timer_on = False

philip_timer = Timer()
philip_timer_on = False

opinion_timer = Timer()
opinion_timer_on = False

timer_randomness = Timer()

playing_timer = Timer()


def setup_timers():

    forest_timer_on = False
    forest_timer.set_duration(15)

    emotional_damage_timer_on = False
    emotional_damage_timer.set_duration(15)

    overig_timer_on = False
    overig_timer.set_duration(90)

    animal_timer_on = False
    animal_timer.set_duration(15)

    philip_timer_on = False
    philip_timer.set_duration(15)

    opinion_timer_on = False
    opinion_timer.set_duration(10)

    timer_randomness.set_duration(30)

    playing_timer.set_duration(3)
