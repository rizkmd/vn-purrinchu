define p = Character("Purrin")
define k = Character("Raja Barat")
define a = Character("Akung")
define x = Character("Xiao Ming Ling")
define pov = Character("[povname]")

label start:
    
    scene bg anime grassland 185

    "Sejak awal terciptanya dunia, manusia hidup berdampingan dengan makhluk-makhluk rakus dari planet lain yang datang melintasi angkasa."
    "Makhluk-makhluk itu terus mengincar Bumi. Mereka ingin menguasai seluruh sumber daya dan kehidupan yang ada."

    scene bg sky_day_dragon

    "Namun, setiap serangan selalu digagalkan oleh seekor naga penjaga Bumi."
    "Naga itu bukan makhluk abadi. Ia beregenerasi setiap 100 tahun."
    "Ketika usianya mencapai 90 tahun, sang naga akan bertelur."

    scene bg sky_day_egg

    "Telur itu harus dijaga selama 10 tahun hingga menetas menjadi naga baru yang cukup kuat untuk melindungi dunia."
    "Selama masa penetasan, telur naga disimpan di tengah kota kecil bernama Cimahi dan dijaga oleh para Dragon Sage."

    scene bg sky_night

    "Suatu malam, seorang raja dari barat mendapat mimpi aneh."

    show k neutral

    k "Hmmm... Mimpi yang menarik."
    k "Siapa pun yang memakan sesuap telur naga ceplok akan memperoleh kekuatan setara sang naga penjaga."
    k "Apa benar?"
    k "Pasti hanya mimpi belaka."

    show k challenging_smile

    k "Tapi aku ini raja yang sakti, tidak mungkin aku memimpikan hal yang tidak masuk akal."

    show k challenging_laugh

    k "Jika aku bisa mendapatkan telur itu, aku akan menjadi penguasa dunia yang tak terkalahkan!"
    
    "Sang raja diam-diam menyiapkan tim elit untuk mencuri telur naga."

    scene bg village
    show a neutral
    
    a "Purrin, anakku..."
    a "Kamu sudah besar sekarang, dan kamu akan menjadi pemimpin Dragon Sage berikutnya."

    hide a neutral
    show p worried_talk

    p "Aku tahu. Tapi kenapa tiba-tiba Akung membicarakan hal ini?"

    hide p worried_talk
    show a sad

    a "Karena aku merasa waktunya sudah dekat. Aku sudah tua, dan aku ingin kamu siap untuk tugas besar ini."

    hide a sad
    show p worried_talk

    p "Tapi, Akung kan masih hidup? Aku juga belum belajar terlalu banyak."

    hide p worried_talk
    show a worried

    a "Aku merasakan ada bahaya besar yang akan datang."
    a "Aku juga sudah terlalu tua untuk melindungi telur naga. Aku ingin kamu siap untuk menghadapi ancaman itu."

    hide a worried
    show a neutral

    a "Aku tahu kamu masih muda, tapi aku percaya kamu bisa melakukannya."
    a "Kamu adalah anakku, dan aku yakin kamu akan menjadi pemimpin Dragon Sage yang hebat."

    hide a neutral
    show p flustered

    p "{i}(Bahaya aoaab dah, dasar orang tua banyak ngelamun){/i}"

    scene bg stasiun

    "Sementara itu, Raja Barat sudah sampai di Cimahi dengan pasukannya."

    show k challenging_laugh

    k "Akhirnya, kita sampai juga di Cimahi."
    k "Aku akan merebut telur naga itu!"

    hide k challenging_laugh
    show k shy_grin

    k "Tapi sebelum itu, kita mi ayam dulu di alun-alun."

    scene bg alun
    show k happy_laugh

    k "Hmm... Ada banyak makanan di sini. Aku ingin mencoba semuanya!"

    hide k happy_laugh
    show x nervous_embarrassed_laugh

    x "Selamat malam, Tuan. Sepertinya Anda baru di sini."
    x "Apakah Anda ingin mencoba mi ayam kami? Ini adalah makanan khas Cimahi yang sangat lezat!"

    hide x nervous_embarrassed_laugh
    show k shy_grin

    k "Memang itu tujuanku datang ke sini. Aku ingin mencoba mi ayam kalian."
    k "Setelah itu, aku ingin melihat telur naga."

    hide k shy_grin
    show x nervous_embarrassed_laugh

    x "Kami tidak mengizinkan orang luar mendekati telur naga. Telur itu sangat berharga."
    x "Orang luar hanya bisa melihat telur jika ada Dragon Sage yang menemani."
    x "Perizinannya diproses selama 14 hari kerja."
    x "Tapi Tuan beruntung, aku bisa menemanimu untuk melihat telur itu sekarang juga."

    hide x nervous_embarrassed_laugh
    show k shy_grin

    k "{i}(Wow, gadis ini adalah Dragon Sage!){/i}"
    k "Oh, begitu ya. Kamu baik sekali."
    k "Siapa namamu?"

    hide k shy_grin
    show x nervous_embarrassed_laugh

    x "Namaku Xiao Ming Ling. Namamu siapa, Tuan?"

    hide x nervous_embarrassed_laugh
    show k shy_grin

    k "Terima kasih, Xiao Ming Ling."
    k "Kamu bisa memanggilku Barat."

    scene bg dprd_egg

    "Xiao Ming Ling mengantarkan Raja Barat ke gedung tempat telur naga disimpan."

    show k challenging_smile
    k "{i}(Itu dia, telur naga diletakkan di atap gedung!{/i})"

    hide k challenging_smile
    show x nervous_embarrassed_laugh

    x "Baiklah, kita sudah sampai."

    hide x nervous_embarrassed_laugh
    show k happy_laugh

    k "Wow, itu dia telur naga! Persis seperti yang terlihat di mimpiku!"
    k "Xiao Ming Ling, aku dengar telur naga dijaga dengan ketat oleh para Dragon Sage."
    k "Tapi aku tidak melihat ada Dragon Sage lain di sini."

    hide k happy_laugh
    show x nervous_embarrassed_laugh

    x "Sebenarnya, telur naga tidak dijaga seperti yang kamu bayangkan."
    x "Kami tidak menjaga dengan pasukan bersenjata atau semacamnya."
    x "Tapi kami menjaga suhu, kelembaban, dan kondisi lainnya agar telur itu bisa menetas dengan baik."
    x "Lagi pula, jika orang luar mencurinya, mereka tidak akan bisa melakukan apa-apa dengan telur itu."

    hide x nervous_embarrassed_laugh
    show k neutral

    k "Oh... Tidak kusangka akan semudah ini."

    hide k neutral
    show x neutral_talk

    x "Huh?"

    hide x neutral_talk
    show k angry_talk

    k "Prajurit..."

    hide k angry_talk
    show k very_angry_talk

    k "SERANG DIA!"

    hide k very_angry_talk
    show kings warrior

    "CIATTTT!!!"

    hide kings warrior
    show x scared_talk_dead

    x "Aaaahhh!!!"

    scene bg stasiun
    show k challenging_laugh

    k "Hahaha! Aku berhasil mencuri telur naga itu!"
    k "Gadis yang baik, namun bodoh."
    k "Sekarang aku akan menjadi penguasa dunia yang tak terkalahkan!"
    k "Mari kita pulang ke barat."

    scene bg dprd
    show a neutral

    a "Selamat pagi, dunia."

    hide a neutral
    show a surprised

    a "KEMANA TELUR NAGA ITU?!"

    hide a surprised
    show a worried

    a "Uhuk... Uhuk..."
    
    hide a worried
    show p worried_talk

    p "Akung, ada apa?"
    p "Pagi-pagi begini sudah teriak-teriak."

    hide p worried_talk
    show a angry

    a "TELUR NAGA HILANG!!!"

    hide a angry
    show p disbelief

    p "Nani the fuck?!"

    hide p disbelief
    show x scared_talk

    x "Akung, Purin, maaf..."

    hide x scared_talk
    show a angry

    a "XIAO MING LING"
    a "APA YANG TERJADI?"
    a "DAN KENAPA TUBUHMU PENUH LUKA?"

    hide a angry

    "Xiao Ming Ling menceritakan apa yang terjadi."

    show a worried

    a "Aku tidak tahu harus berkata apa..."
    a "Raja Barat mencuri telur naga!"
    a "Apa yang dia pikirkan?!"

    show a sad

    a "Uhuk... Uhuk..."
    a "Purrin, aku sudah terlalu tua untuk menghadapi ini."
    a "Kamu harus merebut telur itu kembali."
    a "Pergilah bersama Xiao Ming Ling."
    a "Sebelum kalian pergi, berikan beberapa pertanyaan kepada para Dragon Sage muda."
    a "Lalu ajak satu orang dengan pengetahuan di atas rata-rata untuk menemani kalian."

    hide a sad
    show p frown

    p "Baik, Akung. Aku akan melakukan yang terbaik."
    p "Ayo Ming, kita temui para Dragon Sage muda itu satu per satu."
    p "Selamat tinggal, Akung."

    hide p frown
    show a sad

    a "Selamat jalan, semoga kalian berhasil."

    scene bg village
    show p sad_talk

    p "Ming, kita telah menanyai para Dragon Sage muda, tapi tidak ada yang bisa menjawab semua pertanyaanku."
    
    hide p sad_talk
    show x neutral_talk

    x "Kita tidak boleh menyerah, Purrin."
    x "Masih ada satu orang yang belum kita temui."
    x "Itu, yang diam sendirian di pojokan!"

    hide x neutral_talk
    show p neutral_talk

    p "Hey, kamu yang di pojokan!"
    p "Siapa namamu?"

    $ povname = renpy.input("Siapa namamu?: ")
    hide p neutral_talk

    pov "Namaku [povname]"

    show p neutral_talk
    p "Salam kenal, [povname]. Aku Purrin, dan ini Ming."

    hide p neutral_talk
    show x neutral_talk

    x "Halo, [povname]. Aku Xiao Ming Ling."

    hide x neutral_talk
    show p neutral_talk

    p "[povname], seperti yang sudah kamu ketahui, telur naga telah dicuri oleh Raja Barat."
    p "Aku dan Ming sedang mencari seseorang yang bisa membantu kami merebut kembali telur itu."
    p "Jika kamu berhasil menjawab semua pertanyaanku, berarti kamu layak untuk ikut dalam misi ini."
    p "Apakah kamu siap untuk menjawab pertanyaanku?"

    menu:
        "Siap":
            pass
        "Tidak siap":
            hide p neutral_talk
            "Kamu menolak untuk menjawab pertanyaan Purrin."
            "Purrin dan Xiao Ming Ling pergi meninggalkanmu di pojokan."
            "2 hari kemudian, kamu mendapat kabar bahwa mereka tewas dalam perjalanan merebut kembali telur naga."
            "Telur naga tetap hilang, dan bumi kehilangan penjaganya."
            "Peradaban manusia akan punah dalam 10 tahun ke depan."
            "Game Over"
            return

    p "Baiklah, aku akan mulai dengan pertanyaan pertama."
    # This ends the game.

    return
