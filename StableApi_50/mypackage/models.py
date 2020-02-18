# models.py
__all__ = ['projectile']

class Projectile(object):
	def __init__(self, mass, velocity):
		self.mass = mass
		self.velocity = velocity
