import unittest 
import otp_version1 as OTP 
import senders_data 


class TestingOTPSender(unittest.TestCase): 
    
    def assertBetween(self, x, low, hi): 
        if not (low <= x <= hi): 
            raise AssertionError( 'Length of OTP should be in between %r and %r' % (low, hi)) 
    
    def test_generate_OTP(self): 
        size = 5 
        otp = OTP.generate_OTP(size) 
        self.assertEqual(len(otp), size, 'OTP length does not match') 
        self.assertBetween(len(otp), 4, 8) 
    
    '''def test_verifyOTP(self): 
        otp = OTP.generateOTP(4) 
        self.assertTrue(OTP.verifyOTP(otp, otp), "OTP does not match") 
        self.assertFalse(OTP.verifyOTP(otp, 'abcd'), "OTP should not have matched") 
    '''
    def test_validateEmail(self): 
        receiver_email = 'username@domain.in' 
        self.assertIn('@', receiver_email, "Email is not valid") 
        self.assertIn('.in', receiver_email, "Email is not valid") 
    
    def test_validateEmail2(self): 
        receiver_email = 'username@domain.com' 
        self.assertIn('@', receiver_email, "Email is not valid") 
        self.assertIn('.com', receiver_email, "Email is not valid") 
    
    def test_send_email(self): 
        otp = OTP.generate_OTP(5) 
        receiver_email = 'sakshipjadhav118@gmail.com' 
        receivers_name= 'Sakshi'
        self.assertBetween(len(otp), 4, 8) 
        self.assertIn('@', receiver_email, "Email is not valid") 
        self.assertIn('.com', receiver_email, "Email is not valid") 
        OTP.send_email(senders_data,receivers_name, receiver_email, otp) 


if __name__ == '__main__': 
 unittest.main() 