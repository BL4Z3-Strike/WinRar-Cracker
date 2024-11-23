import rarfile

def crack_rar(rar_filename, wordlist_filename):
    # RAR dosyasını açıyoruz
    with rarfile.RarFile(rar_filename) as rar_file:
        # Şifre listemizi açıyoruz
        with open(wordlist_filename, 'r') as wordlist:
            for password in wordlist:
                password = password.strip()  # Boşlukları ve satır sonlarını temizliyoruz
                try:
                    # Şifreyi set ediyoruz
                    rar_file.setpassword(password)
                    
                    # Dosyayı çıkarmayı deneyelim (burada şifreyi test ediyoruz)
                    rar_file.extract(rar_file.namelist()[0])  # İlk dosyayı çıkarıyoruz
                    
                    print(f"Password found: {password}")
                    return password  # Şifre bulunduğunda çıktıyı veriyoruz
                except rarfile.BadRarFile:
                    # Şifre yanlışsa devam ediyoruz ve bir sonraki şifreyi deniyoruz
                    continue
                except Exception as e:
                    # Hataları yakalıyoruz
                    print(f"An error occurred: {e}")
                    continue
    print("Password not found.")
    return None

if __name__ == '__main__':
    rar_filename = 'myfile.rar'  # Şifresi kırılacak RAR dosyasının adı
    wordlist_filename = 'wordlist.txt'  # Kullanılacak şifreler listesi
    crack_rar(rar_filename, wordlist_filename)
