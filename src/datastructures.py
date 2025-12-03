class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        keys_to_check = ["first_name", "age", "lucky_numbers"]
        #Check if all information was provided
        if all(key in member for key in keys_to_check):
            new_member = {
                "id": self._generate_id(),
                "first_name": member["first_name"],
                "last_name": self.last_name,
                "age": member["age"],
                "lucky_numbers": member["lucky_numbers"]
            }
            self._members.append(new_member)
            return new_member
        #If not return a string with the error
        return "Member information missing or incorrect"

    def delete_member(self, id):
        #Check if member is in the list per id
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return {
                    "done": True
                }  
        #If not return a string with the error
        return "ID not found"

    def get_member(self, id):
        #Check if member is in the list per id
        for member in self._members:
            if member["id"] == id:
                return member
        #If not return a string with the error
        return "ID not found"

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members