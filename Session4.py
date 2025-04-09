
def main():
	class FavoriteAnimal:
		def __init__(self, arm_length , leg_length, num_eyes, has_tail, is_furry):
			self.arm_length = arm_length
			self.leg_length = leg_length
			self.num_eyes = num_eyes
			self.has_tail = has_tail
			self.is_furry = is_furry

		def describe(self):
			print("Animal Characteristics:")
			print(f"- Arm length: {self.arm_length} units")
			print(f"- Leg length: {self.leg_length} units")
			print(f"- Number of eyes: {self.num_eyes}")
			print(f"- Has tail: {'yes' if self.has_tail else 'No'}")
			print(f"- Is furry: {'yes' if self.is_furry else 'No'}")

	my_fav_animal = FavoriteAnimal(
			arm_length = 24,
			leg_length = 62,
			num_eyes = 2,
			has_tail = False,
			is_furry = True
			)

	my_fav_animal.describe() #Animal is:Capybara :)



if __name__ == "__main__":
	main()