from faker import Faker
from .create_vietnamese_corpus import write_to_file


class DataGeneration:
    def __init__(self, vocab_file_path):
        self.fake = Faker()
        self.vocab_file = vocab_file_path
        Faker.seed(0)

    def generate_license_plate(self, num):
        """
        TKG 876'
        'VZJ3824'
        'CUZ N92'
        '5S 7815X'
        '8PX7784'
        """
        license_plate = []
        for _ in range(num):
            license_plate.append(self.fake.license_plate())
        return license_plate

    def generate_credit_card_number(self, num):
        """
        '4604876475938242'
        '5248924115781561'
        '4387784080167'
        '180009753513939'
        '4871158714841859'
        """
        credit_card_number = []
        for _ in range(num):
            credit_card_number.append(self.fake.credit_card_number())
        return credit_card_number

    def generate_bban_number(self, num):
        """
        'VTKG87647593824219'
        'UZNS92411578156593'
        'ZMWG80160975351393'
        'GZUL15871484185839'
        'OHCU59342320947112'
        """
        bban_num = []
        for _ in range(num):
            bban_num.append(self.fake.bban())
        return bban_num

    def generate_swift_code(self, num):
        """
        'TKGNGBO2KRV'
        'NHTQGBJ6936'
        'SXRMGBDP'
        'XZMWGBJ2TAZ'
        'VRAMGB5I'
        """
        swift_code = []
        for _ in range(num):
            swift_code.append(self.fake.swift())
        return swift_code

    def generate_msisdn(self, num):
        """
        '6048764759382'
        '1948924115781'
        '5938778408016'
        '0975351393328'
        '1587148418583'
        """
        msisdn = []
        for _ in range(num):
            msisdn.append(self.fake.msisdn())
        return msisdn

    def generate_int(self, num):
        """
        6311
        6890
        663
        4242
        8376
        """
        int_num = []
        for _ in range(num):
            int_num.append(self.fake.pyint(min_value=0, max_value=10000000000000000))
        return int_num

    def generate_str(self, num):
        """
        'RNvnAvOpyEVAoNGnVZQU'
        'qLUJyfwFVYySnPCaLuQI'
        'azTmqTjDmYPxeqAWfCKC'
        'QCYFExFuDpjjFIyeNTWR'
        'UWCuKoQSUEXExIZVPeFz'
        """
        str_list = []
        for _ in range(num):
            str_list.append(self.fake.pystr())
        return str_list

    def generate_vocab(self):
        license_plate_num = 1
        credit_card_number_num = 1
        bban_number_num = 1
        swift_code_num = 1
        msisdn_num = 1
        int_num = 1
        str_num = 1
        total_vocab = []
        total_vocab.extend(self.generate_license_plate(license_plate_num))
        total_vocab.extend(self.generate_credit_card_number(credit_card_number_num))
        total_vocab.extend(self.generate_bban_number(bban_number_num))
        total_vocab.extend(self.generate_swift_code(swift_code_num))
        total_vocab.extend(self.generate_msisdn(msisdn_num))
        total_vocab.extend(self.generate_int(int_num))
        total_vocab.extend(self.generate_str(str_num))
        print('Total: ', len(total_vocab))
        total_vocab = list(set(total_vocab))
        print('After: ', len(total_vocab))
        write_to_file(total_vocab, self.vocab_file)