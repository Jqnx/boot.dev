def take_magic_damage(health, resist, amp, spell_power):
    dmg = (spell_power * amp) - resist
    new_health = health - dmg
    return new_health
