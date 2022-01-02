class Dni:
    def __init__(self, new_dni=""):
        self.dni = new_dni
        self.table = "TRWAGMYFPDXBNJZSQVHLCKE"

    ##### interfaz PUBLICA #####
    def set_dni(self, new_dni):
        self.dni = new_dni

    def get_dni(self):
        return self.dni

    def check_is_valid(self):
        if not self.calculate_letter():
            return False
        return self.get_dni_letter() == self.calculate_letter()

    def get_letter(self):
        if self.check_dni_format():
            return self.get_dni_letter()

    ##### parte PRIVADA #####
    def get_dni_letter(self):
        return self.dni[-1]

    def get_dni_number(self):
        return self.dni[:-1]

    def calculate_letter(self):
        if self.check_dni_format():
            return self.table[int(self.get_dni_number()) % len(self.table)]

    def check_dni_format(self):
        if type(self.dni) == str and self.dni:
            return self.get_dni_number().isdigit() and len(self.dni) == 9


if __name__ == "__main__":
    bad_dnis = [
        "",
        "12345A",
        "12345678A",
        12345,
        "03297533U",
        "a9a39(JL:",
        ["asd", "djksja"],
        {1: "l", 2: "l"},
        None,
        "78484464E",
        "72376173Q",
        "01817200A",
        "95882054T",
    ]

    good_dnis = [
        "78484464T",
        "72376173A",
        "01817200Q",
        "95882054E",
        "63587725Q",
        "26861694V",
        "21616083Q",
        "26868974Y",
        "40135330P",
        "89044648X",
        "80117501Z",
        "34168723S",
        "76857238R",
        "66714505S",
        "66499420A",
    ]

    def format_test_dni(test_dni):
        print("DNI is -->", test_dni.get_dni())
        print("DNI Entered Letter is -->", test_dni.get_letter())
        print("DNI Correct Letter is -->", test_dni.calculate_letter())
        print(
            "So, the DNI is -->",
            "Valid" if test_dni.check_is_valid() else "Not Valid",
            "\n",
        )

    print("Bad DNIs")
    for dni in bad_dnis:
        test_dni = Dni(dni)
        format_test_dni(test_dni)
        assert test_dni.check_is_valid() is False

    print("Good DNIs")
    for dni in good_dnis:
        test_dni = Dni(dni)
        format_test_dni(test_dni)
        assert test_dni.check_is_valid() is True
