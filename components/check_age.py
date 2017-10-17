from meya import Component

class AgeChecker(Component):

    def start(self):
        age = self.db.flow.get('age')
        try:
            age = int(age)
        except:
            age = 0

        action = 'over' if age > 17 else 'under'
        return self.respond(message=None, action=action)
