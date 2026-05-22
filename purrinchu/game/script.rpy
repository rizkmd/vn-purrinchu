# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Purrin")
define k = Character("Raja Barat")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene bg anime grassland 185

    "Sejak awal terciptanya dunia, manusia hidup berdampingan dengan makhluk-makhluk rakus dari planet lain yang datang melintasi angkasa."
    "Makhluk-makhluk itu terus mengincar Bumi. Mereka ingin menguasai seluruh sumber daya dan kehidupan yang ada."

    scene bg sky_day_dragon

    "Namun, setiap serangan selalu digagalkan oleh seekor naga penjaga Bumi."
    "Naga itu bukan makhluk abadi. Ia beregenerasi setiap 100 tahun."
    "Ketika usianya mencapai 90 tahun, sang naga akan bertelur."

    scene bg sky_day_egg

    "Telur itu harus dijaga selama 10 tahun hingga menetas menjadi naga baru yang cukup kuat untuk melindungi dunia."
    "Selama masa penetasan, telur naga disimpan di tengah kota kecil bernama Cimahi dan dijaga ketat oleh para Dragon Sage."

    scene bg sky_night

    "Suatu malam, seorang raja dari barat mendapat mimpi aneh."

    show king neutral

    k "Hmmm... Mimpi yang menarik."
    k "Siapa pun yang memakan sesuap telur naga ceplok akan memperoleh kekuatan setara sang naga penjaga."
    k "Apa benar?"
    k "Pasti hanya mimpi belaka."

    show king challenging_smile

    k "Tapi aku ini raja yang sakti, tidak mungkin aku memimpikan hal yang tidak masuk akal."

    show king challenging_laugh
    k "Jika aku bisa mendapatkan telur itu, aku akan menjadi penguasa dunia yang tak terkalahkan!"
    
    "Sang raja diam-diam menyiapkan pasukan dan menunggu waktu yang tepat untuk menyerbu Cimahi demi merebut telur naga."


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

    

    # This ends the game.

    return
