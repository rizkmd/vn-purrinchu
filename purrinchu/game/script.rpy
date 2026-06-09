define p = Character("Purrin")
define k = Character("Raja Barat")
define a = Character("Akung")
define x = Character("Xiao Ming Ling")
define pov = Character("[povname]")
define o1 = Character("???")
define o2 = Character("Bukan Akung")
define g = Character("???")
define t = Character("Tono")

default current_question_idx = 0
default score = 0
default player_response = ""

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

    call make_question_list from _call_make_question_list   # build the list
    $ current_question_idx = 0                              # reset counter
    $ score = 0
    jump begin_quiz                                         # start the quiz


label begin_quiz:

    if current_question_idx >= len(question_list):
        jump quiz_finished

    $ current_question = question_list[current_question_idx]
    $ adjusted_idx = current_question_idx + 1

    p "Pertanyaan [adjusted_idx]: [current_question.question]"

    menu:
        "[current_question.a1]":
            $ player_response = current_question.a1
            #call check_answer from _call_check_answer

        "[current_question.a2]":
            $ player_response = current_question.a2
            #call check_answer from _call_check_answer_1

        "[current_question.a3]":
            $ player_response = current_question.a3
            #call check_answer from _call_check_answer_2

        "[current_question.a4]":
            $ player_response = current_question.a4
            #call check_answer from _call_check_answer_3

#label check_answer:

    if player_response == current_question.correct:
        p "Hmm..."
        $ score += current_question.point_value
    else:
        p "Hmm..."

    $ current_question_idx += 1
    jump begin_quiz


label quiz_finished:

    p "Kamu menjawab semua pertanyaan dengan skor [score] dari [len(question_list)]."

    if score >= 8:   # all correct
        hide p neutral_talk
        show p happy_talk
        p "Luar biasa! Kamu layak ikut dalam misi ini."
        jump continue_game
    else:
        p "Hmm... Kamu masih perlu banyak belajar."
        hide p neutral_talk
        "Purrin dan Xiao Ming Ling pergi meninggalkanmu di pojokan."
        "2 hari kemudian, kamu mendapat kabar bahwa mereka tewas dalam perjalanan merebut kembali telur naga."
        "Telur naga tetap hilang, dan bumi kehilangan penjaganya."
        "Peradaban manusia akan punah dalam 10 tahun ke depan."
        "Game Over"
        return

label continue_game:
    p "Baiklah, kita akan segera memulai perjalanan ini."

    scene bg anime grassland 9
    
    "Purrin, Xiao Ming Ling, dan [povname] melakukan perjalanan selama beberapa hari."
    "Perjalanan berlangsung cukup tenang."
    "Mereka melewati padang rumput luas dan beberapa desa kecil."

    scene bg anime grassland 10

    "Saat matahari mulai terbenam, dari kejauhan terlihat sebuah desa yang ramai."
    "Lampion tergantung di sepanjang jalan, dan suara musik serta tawa terdengar dari dalam desa."

    show p happy_talk

    p "Wow, sepertinya ada festival di desa itu!"
    p "Ayo kita lihat!"

    menu:
        "Ayo!":
            pass
        "Tidak, kita harus fokus berjalan ke barat!":
            jump continue_game_no_festival

    p "Kita sudah berjalan jauh, kita pantas mendapatkan sedikit hiburan!"

    scene bg festival
    show p happy_talk
    p "Ini luar biasa! Aku senang kita memutuskan untuk mampir!"

    hide p happy_talk
    show x nervous_embarrassed_laugh

    x "Lihat, ada banyak makanan enak di sini!"

    hide x nervous_embarrassed_laugh
    show p happy_talk

    p "Dan lihat, ada pertunjukan musik dan tarian yang keren!"

    hide p happy_talk
    show x nervous_embarrassed_laugh

    x "Ada permainan juga, ayo kita coba!"

    scene bg festival_game

    "Purrin, Xiao Ming Ling, dan [povname] menikmati berbagai kegiatan di festival itu."
    "Mereka bermain permainan, menonton pertunjukan, dan mencicipi makanan lezat."

    show p happy_talk

    p "Ah, aku sudah kenyang dan mulai lelah."
    p "Tapi sebelum kita lanjut, aku ingin [povname] untuk membuktikan sekali lagi bahwa kamu layak ikut dalam misi ini."
    p "Aku ingin kamu memainkan salah satu permainan di festival ini dan menang."

    hide p happy_talk

    pov "Kalo cuma permainan festival mah gampang, aku pasti menang!"

label card_game_gate:
    $ card_game = CardMatchGame(pairs=6)
    call screen card_match_game(card_game)

    if _return:
        show p happy_talk
        p "Wah, hebat! Kamu berhasil mencocokkan semua kartu!"
        p "Memori yang tajam seperti ini akan sangat berguna dalam misi kita."
        pass
    else:
        show p neutral_talk
        p "Hmm, kamu menyerah? Ayo coba lagi, pasti bisa!"
        hide p neutral_talk
        jump card_game_gate

p "Baiklah, kita sudah cukup bersenang-senang di festival ini."
p "Saatnya istirahat."
p "Kita lanjutkan perjalanan ke barat besok pagi."

hide p happy_talk
show o

o1 "Jarang sekali melihat petualang menuju barat akhir-akhir ini."

hide o
show p surprised_talk

p "Eh... Bukankah ini mY?!"

hide p surprised_talk
show o

o1 "My my apa maksudmu anak muda?"

hide o
show p surprised_talk

p "My Akung?"

hide p surprised_talk
show o

o1 "Siapa Akung? Aku bukan Akung!"

hide o
show p happy_talk

p "Akung lucu sekali, pakai kacamata hitam dan dasi kupu-kupu."

hide p happy_talk
show o

o1 "Aku bukan Akung!"

hide o
show p neutral_talk

p "Lalu kamu siapa?"

hide p neutral_talk
show o

o1 "Tidak penting siapa aku, yang penting aku bukan Akung!"

hide o
show p neutral_talk

p "Baiklah, bukan Akung."
p "Kenapa tidak ada petualang yang menuju ke barat akhir-akhir ini?"

hide p neutral_talk
show o

o2 "Banyak berita buruk."
o2 "Para pedagang yang pergi ke barat tidak ada yang kembali."
o2 "Padahal, biasanya mereka pulang paling lama 3 hari."
o2 "Kami mencoba untuk mencari mereka di hutan, tapi tidak menemukan apa-apa."

hide o
show x neutral_talk

x "Apakah itu ulah monster hutan?"

hide x neutral_talk
show o

o2 "Monster biasanya meninggalkan jejak."
o2 "Yang ini tidak."
o2 "Lagipula, puluhan tahun aku hidup, tidak pernah ada monster di hutan itu."
o2 "Aku rasa ada sesuatu yang salah di barat."

hide o
show x neutral_talk

x "Purrin... Aku takut."

hide x neutral_talk
show p frown

p "Tidak apa-apa, Ming."
p "Kita akan menghadapi apapun yang ada di barat bersama-sama."
p "Terima kasih atas informasinya, Bukan Akung."

hide p frown
show o

o2 "Berhati-hatilah, anak muda."
o2 "Oyasumi."

scene bg sky_night

"Purrin, Xiao Ming Ling, dan [povname] mendirikan tenda dan segera berbaring tanpa berkata sepatah kata pun."

show x neutral_talk

x "{i}(Aku sangat takut...){/i}"
x "{i}(Ini semua salahku){/i}"
x "{i}(Aku yang membuat Raja Barat mencuri telur naga){/i}"
x "{i}(Dan sekarang aku membuat Purrin, [povname], dan seisi dunia dalam bahaya){/i}"

hide x neutral_talk
show p frown

p "{i}(Aku juga takut, Ming){/i}"
p "{i}(Tapi aku harus tetap kuat untukmu dan [povname]){/i}"
p "{i}(Apa pun yang terjadi, aku harus melindungi kalian){/i}"
p "{i}(Dan seisi dunia...){/i}"

hide p frown

pov "{i}(Kenyang banget bjir){/i}"

scene bg anime grassland 9
show x nervous_embarrassed_laugh

x "Selamat pagi, Purrin."
x "Selamat pagi, [povname]."
x "Kalian sudah siap untuk melanjutkan perjalanan kita hari ini?"

hide x nervous_embarrassed_laugh
show p happy_talk

p "Yuk!"

hide p happy_talk

"Tanpa mereka sadari, dari kejauhan ada sosok misterius yang mengawasi."

show g

g "Mereka benar-benar menuju ke barat."
g "Aku akan mengirim surat pada Raja..."

scene bg hutan
show x neutral_talk

x "Inikah hutan yang dimaksud Bukan Akung?"

hide x neutral_talk
show p neutral_talk

p "Sepertinya iya. Tapi jangan takut, Ming"
p "Bukan Akung bilang tidak ada monster di sini, jadi kita harusnya aman."

hide p neutral_talk
show x neutral_talk

x "Tapi, bagaimana jika ada hantu?"

hide x neutral_talk
show p neutral_talk

p "Percayalah aku bisa lebih menghantui dari hantu."

hide p neutral_talk

pov "Aku percaya."

show p angry

p "Heh!"

hide p angry
show x blush_happy_laugh

x "Hahaha..."

hide x blush_happy_laugh
show p shy_smile

p "{i}(Akhrinya Ming bisa tersenyum lagi...){/i}"

scene bg anime grassland 18
show x nervous_embarrassed_laugh

x "Akhirnya kita keluar dari hutan menakutkan itu!"
x "Lihat, seperti ada tenda di depan sana!"

hide x nervous_embarrassed_laugh
show p happy_talk

p "Ayo kita lihat!"

scene bg camp
show p neutral_talk

p "Ada yang tidak beres."
p "Tidak ada tanda-tanda pertempuran, darah, apalagi mayat."
p "Hanya ada tenda yang ditinggalkan begitu saja."
p "Lihat, ada sekantung penuh uang. Ini juga bukan perampokan."

hide p neutral_talk

"Tidak ada yang bisa menjawab."
"Semakin jauh mereka berjalan ke barat, semakin sering mereka melihat tenda-tenda seperti itu."
"Tenda yang kosong, api unggun yang sudah padam."
"Barang-barang tak bertuan."
"Seolah ditinggalkan begitu saja."

scene bg anime grassland 33

"Sore hari tiba, Xiao Ming Ling tampak gelisah."

show x neutral_talk

x "Purrin, [povname], aku merasa seperti mendengar seseorang."

hide x neutral_talk

"Mereka berhenti sejenak, mencoba mendengar dengan seksama."

pov "Aku juga mendengar sesuatu..."

show p neutral_talk

p "Seperti seseorang sedang bernyanyi."
p "Ayo kita datangi suara itu!"

hide p neutral_talk
show x neutral_talk

x "Bagaimana jika itu adalah jebakan?"

hide x neutral_talk

menu:
    "Aku setuju dengan Purrin":
        pass
    "Xiao Ming Ling benar, ayo tetap berjalan lurus!":
        "Mereka pun terus berjalan ke barat tanpa mendatangi suara itu."
        "Mereka tidak pernah tahu apa yang mereka lewatkan."
        "Namun, di dalam hati ketiganya sangat penasaran."
        "Mereka pun mati penasaran."
        "Game Over"
        return

"Mereka mengikuti suara itu dan menemukan seseorang di balik batu."

show t surprised

t "Ah, kalian menemukanku!"

hide t surprised
show p neutral_talk

p "Tentu saja kami menemukanmu, nyanyianmu terdengar dari ujung sana!"

hide p neutral_talk
show t surprised

t "Iya kah? Padahal aku sudah berusaha menyanyikan dengan pelan supaya tidak terdengar terlalu jauh."
t "Apa yang kalian lakukan di tempat berbahaya seperti ini?"

hide t surprised
show p neutral_talk

p "Bahaya apa yang mengancam tempat ini?"
p "Dan kenapa kamu sendirian di tempat yang kau bilang berbahaya?"

hide p neutral_talk
show t neutral

t "Namaku Tono, seorang penyanyi jalanan."
t "Aku ingin sekali bernyanyi di Kerajaan Barat. Orang-orang di desa melarangku untuk pergi karena banyak pedagang yang tidak kembali dari sana."
t "Tapi aku tidak peduli. Bagiku, misteri itu akan menjadi cerita yang bagus untuk lagu-laguku."

hide t neutral
show p neutral_talk

p "Lalu?"

hide p neutral_talk
show t blush

t "Lalu aku melihat tenda yang kosong itu, dan aku pun ketakutan."

hide t blush

menu:
    "Hahaha cupu":
        "Purrin, Xiao Ming Ling, dan Tono marah padamu karena kamu tidak sopan."
        "Mereka memukulimu hingga mati."
        "Game Over"
        return
    "Aku mengerti, ayo kita tetap bersama!":
        pass

show t blush

t "Benarkah?"

hide t blush
show x blush_happy_laugh

x "Kami juga ingin pergi ke barat. Aku merasa lebih aman jika lebih banyak orang yang pergi bersama."
x "Boleh kan, Purrin?"

hide x blush_happy_laugh
show p frown_smile

p "Tentu saja. Tono, ayo bergabung dengan kami!"

hide p frown_smile
show t happy

t "Terima kasih, teman-teman baruku!"
t "Aku tau kita belum saling kenal satu sama lain, tapi aku lebih takut ditinggalkan sendirian di tempat ini."
t "Jadi, siapa kalian dan kenapa kalian pergi ke barat?"

hide t happy

"Purrin, Xiao Ming Ling, dan [povname] memperkenalkan diri kepada Tono."
"Namun, mereka tidak menceritakan tentang misi mereka untuk merebut kembali telur naga."
"Mereka hanya mengatakan bahwa mereka senang berpetualang."


label continue_game_no_festival:
    p "Kamu benar, kita harus fokus pada tujuan kita."
    

    return
