def take_magic_damage(health, resist, amp, spell_power):
    max_damage = spell_power * amp
    damage = max_damage - resist
    return health - damage
