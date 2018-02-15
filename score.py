#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ドライバをimport
import MySQLdb
import csv
if __name__ == '__main__':
    #データベース接続
    connect = MySQLdb.connect(host='127.0.0.1', db='sotuken', user='root', passwd='teikyo', charset='utf8')
    #ハンドル
    cursor = connect.cursor()
    h = connect.cursor()
    b = connect.cursor()
    c = connect.cursor()
    d = connect.cursor()
    e = connect.cursor()
    f = connect.cursor()
    g = connect.cursor()

    sql1= "select * from jiminto"
    sql2 = "select * from rikkennminshuto"
    sql3= "select * from nihon_isin_no_to"
    sql4= "select * from nihonkyosanto"
    sql5= "select * from minshinto"
    sql6= "select * from koumeito"
    sql7= "select * from kibounoto"

    h.execute(sql1)  # select文を実行
    b.execute(sql2)
    c.execute(sql3)
    d.execute(sql4)
    e.execute(sql5)
    f.execute(sql6)
    g.execute(sql7)

    #左翼用単語辞書
    sayoku_tango=["核兵器","禁止","条約","教育","衆院","市長","安倍","沖縄","事故","日本","政府","対応","国際","問題","市民","名護","訴え",
    "未来","選挙","政治","改憲","憲法","訪問","ノーベル","平和","辺野古","基地","廃絶","企業","懇談","予算","本部","会長","消費","署名",
    "原発","参院","都議","世論","赤旗","北朝鮮","対話","解決","国会","推進","首相","建設","野党","共闘","参議院","政権","労働","国民",
    "共同","政策","反対","稼働","意見","国連","会議","対策","要請","撤回","貧困","カジノ","補選","移転","質問","中止","被害","危険","築地",
    "普天間","トランプ","代表","介護","立憲","保険","規制","健康","病院","医療","医師","保有","防止","基準","障害","改悪","年金","規制","改正",
    "組合","不足","廃止","雇用","難病","福祉","改定","起訴","アスベスト","高裁","判決","無期","転換","契約","避難","過労","主義","歴史",
    "勝利","絶対","軍機","落下","保育園","事実","墜落","攻撃","韓国","大統領","米国","エルサレム","軍事","共産","支援","批判","保護",
    "自衛隊","森友","疑惑","容認","究明","改革","連合","躍進","私物化","加計","戦争","自公","朝日新聞","議席","支持","書記","被災","地方",
    "活動","市議","災害","連帯","増税","退場","保障"]

    #右翼用単語
    uyoku_tango=["議長","憲法","改正","推進","問題","地域","中小","商店","事業","継承","消費","軽減","参院","選挙","公約","国土","強靭",
    "強化","北朝鮮","防災","対策","要望","予算","エネルギー","戦略","都議","総務","市長","県議","市議","政調","企業","政策","支援","応援",
    "当選","政権","女性","世代","社会","保育","後援","日本","振興","視察","国際","産業","農業","税制","課税","安倍","総理","国会","介護",
    "国家","内閣","幹部","希望","政党","政治","政務","責任","自公","財政","幼児","教育","無償","財源","討論","未来","重点","金融","国民",
    "党首","政府","努力","コートジボワール","情勢","邦人","安全","意見","ジブチ","海賊","対処","技術","中国","関心","維新","トランプ","大統領",
    "国防","世界","外交","現場","外務","与党","アフリカ","情報","影響","訪日","首脳","成果","松井","会談","経済","改革","被災","イラン","自衛隊",
    "太平洋","領土","艦隊","中東","東日本","大震災","大使館","首相","ドゥテルテ","フィリピン","防衛","大使","基地","派遣","医療","外務省","経験",
    "安定","米国","部隊","韓国","圧力","連携","航空","軍事","サウジ","批判","海軍","予算","竹島","ミサイル","議論","議長","司令","警戒","慰安",
    "危機","発射","実験","皇后","陛下","時代","参拝","女性","国連","活動","言論","男尊女卑","歴史","調査","行政","人口","減少","将来","構想",
    "実現","万博","地方","年金","復活","制度","徹底","許容","姉妹","解消","都市","築地","都構想"]



    #自民党衆参両院
    jiminto_ginlist=["AGP1957","eriko_imai","etoseiichi","fujii_motoyuki","gaku_hasegawa","hanyuda_takashi",
    "hayashi09615064","hiranotatsuo1","ichita_y","IshiiMidori",
    "isozaki_yousuke","isozakiyoshi","AbeShinzo","iwaonarajp","kaeruchikara","katayama_s","kenji_nakanishi",
    "kimurayoshio_","kotaronogami","koyari_shiga","kunikoinoguchi","marukawatamayo",
    "maruyamakun","masahiroishida","masashi_nakano","mat_nakaizumi","matsukawa_rui",
    "miharajunco","miyakeshingo","mizuhoonuma","morimasakosangi","moriyukogiin","motoetaichiro",
    "nakanishiyusuke","ninoyu_satoshi","ninoyutakeshi","ohno_yasutada",
    "okada_naoki","onoda_kimi","satomasahisa","sekiguchi0229","sekohiroshige",
    "shimamuradai","shujimymt","shuko_sonoda","takagaiemiko","takanokohjiro","takashiuto",
    "takemikeizo","takisawamotome","tsuruhoyosuke","wadamasamune","watanabe_miki","yamatanieriko",
    "yamazogaikuzo","yanagimotoosaka","yasutaka_nksn","yasuyukisakai","ykounoike","yoshidahiromi","yoshikawayuumi",
    "55tsutomu2106","244yamaguchi","Hiraki_Daisaku","AbeShinzo",
    "abetoshiko","akibakenya","akimoto_chiba9","akimoto_tsukasa",
    "Akira_Amari","andouhiroshi","doitooru812","ETO_Akinori","etoseishiro",
    "FujiiHisayuki","fukuseikai","funahashi_toshi","ga9_h","genkihoriuchi",
    "GotodaMasazumi","hajime24331","harada_kenji","hatibe47","HatoyamaJiro",
    "hiratakuchan","hiromitsubayasi","hiroyukitogash","hmakihara","hosoda_kenichi",
    "HosodaHiroyuki","hossys","HYT4ALL","iakimasa1","ichiroaisawa","ikeda_0620",
    "iloveyatchan","imaeda_soichiro","ishiharahirotak","IshiharaNobu","itsunori510",
    "iwate_fujiwara","IzumidaHirohiko","junmatsumoto411","kado_wakayama",
    "kajiyamahiroshi","kameokayositami","Kamikawa_Yoko","KAMIYAMA_SAICHI","kanda_kenji",
    "kanke_ichirou","katoayuko_and_s","katsueihirasawa","katsukawai","katsunobukato",
    "Kazuchika_Iwata","kb2474","keiko_nagaoka","keitaro_ohno","kihara_minoru","kihara_seiji",
    "kikawadahitoshi","kimura841","KishiNobuo","kobahawk","kogaatsushi","kokubkonosuke",
    "konotarogomame","kudoshozo","kumadahiromichi","kyoto_honda","makishimakaren",
    "masanobu_ogura","matsumoto_yohei","matusimamidori","MiharaAsahiko","miosugita",
    "mitani_h","mitsuya_office","MiyauchiHideki","miyazawa_japan","moteging","MunekiyoOffice",
    "muraihideki","mutaishunsuke","mutouyouji","nakamurahiro3","nakatani80","NaokazuTakemoto",
    "naomi_tokashiki","nekotanchan","nemotoyukinori","nishy03","nobu_takemura","noda_seiko93",
    "nonakajimusho","norihiron","norikazu_suzuki","norikomiya","ochitakao","odawarakiyoshi",
    "Ogushi_Masaki","ohmisei","onishi_hiroyuki","ryosei_akazawa","saito_hiroaki_","sakai_manabu",
    "SatoYukari","seigo_k","sekiyoshihiro","shiba_masa","ShigekiNara","shigeport",
    "shinako_jimusho","shindo_y","ShinjirouBOT","ShintaroIto205","sonourakentaro","sugawaraisshu",
    "sugawitter","Support_Kamo","SuzukiShunichi","syunsuke_takei","T_Ibayashi",
    "t_kazunori","t_yagi_aichi","tadahiko_itoh","tadamori_oshima","taimei1","TAIRAMASAAKI",
    "takaaki_katsu","takahina7777","takakooendan","takashinagao","takatorishuichi","takeokawamura",
    "Tanaka_Hide","Tanaka_Ryosei","TatsuoFukuda","tatsuyaito0501","Team_e_toshiaki",
    "terada124","TohruIshizaki","Tom_Tanigawa","tujikiyoto","ty_polepole","Ueno_Kenichiro",
    "wakamiya7788","yamada_miki","yamagiwa001","yamamotogiin","YAMASHITA_OK","yasu_shio",
    "yasutaka_nksn","Ymd_Knj","yoshiaki_harada","yoshiiehiroyuki","yoshino_ouen8","yoshiomobi",
    "ysakurada","ywada_hokkaido5"]



    #立憲民主党　衆議院
    rikkennminshuto_ginlist=["9999suematsu","abe_tomoko","AkiHatsushika","akutsuyukihiko","aoyagy","banrikaieda",
    "chinami_niigata","edanoyukio0531","fumiyoshi610","go_shinohara","HasegawaKaichi",
    "ikemakihonki","IshikawaKaori11","kameiakikoweb","kawauchihiroshi","kazu_okajima",
    "kazuma_nakatani","kondo_shoichi","michishitadaiki","MORIYAMAhiro","my_fc1","nagatsumaakira",
    "NaotoKan","NorioKochi","ochiaitakayuki","okamotoakiko","otsujikanako","pontapiranao",
    "rikken_akamatsu","sakurai_shu","sasaki_stop_tpp","SatoshiSatoshiA","seiji_ohsaka",
    "tsujimotokiyomi","waseda_yuki","yamahanaikuo","yamakawa_yuriko","yamauchiko1","yamazakimakoto",
    "yokomitsu_cdp","yoshitune1aichi","YutaHiyoshi"]


    #共産党衆参両院
    nihonkyosanto_ginlist=["buchitom","ichida_t","jcpyamashita","KamiTomoko","kirayoshiko","koike_akira","kotarotatsumi",
    "kurabayashia","mikishi_daimon1","nihi_souhei","pioneertaku84",
    "ryon_t","tamutomojcp","TAMURATAKAAKI","akamineseiken","kokutakeiji","motomura_nobuko",
    "miyamototooru","akibacsi","hatanokimie","shiikazuo","ShiokawaTetsuya","chiduko916"]

    #公明党衆参両院
    koumeito_ginlist=["gagomeyokoyama","HamadaMasayoshi","Hiraki_Daisaku","Hiro_Ishikawa","hisatake_sugi",
    "kumanoseishi","m_nishida","masaaki_taniai","miura_nobuhiro","niizuma_hideki","satomi_ryuji",
    "sayaka_sasaki","t_takeya","takasehiromi163","uozumi_yuichiro","y_hiroshi_1209","Yakura_Katsuo",
    "yamaguchinatsuo","Yamamotokanae","yoshihirokawano","AKBhyogo2ku","hamachi_m","HamamuraSusumu",
    "hidemichisato","Hiro_NAKANO_","InatsuHisashi","isashinichi","ishidanoritoshi","ito_wataru",
    "kitagawa_kazuo","kiyohiko_toyama","Noriko_Furuya","OkamotoOffice","omo_Ukishima","saitotetsuo",
    "shigeki3468","takeuchi_yuzuru","teamohta","ToruKunishige","WanibuchiYoko"]


    #日本維新の党　衆議院
    nihon_isin_no_to_ginlist=["adachiyasushi","baba_ishin","maruyamahodaka","mikioshimoji",
    "MoriNatsue","shiiki_tamotsu_","sugichannet","uranoyasuto"]


    #希望の党　衆議院
    kibounoto_ginlist=["310kakizawa","aoyamayamato","Asano__Satoshi","Fullgen","furumoto_s11","gemmakentaro",
    "green_river15t","hosono_54","imai_masato","junyaog","kanametajima","kazunori_0731",
    "kentarou450417","kiitakashi","komiyama_yasko","kouji_satou","matsubarajin731",
    "mitsunori_ok","mori_morita","nagashima21","nakayamanariaki","nakayasu40","office50824963",
    "oguma_shinji","OogushiHiroshi","sekikenichiro","shinatakeshi","shiraishiyoichi",
    "shuheikishimoto","shunsuke_ishin","sokuno2","tamakiyuichiro","Tsumura_Keisuke","yamanoikazunori",
    "yokomitsu_cdp","yoshiomaki758","yousei_ide","yuichi510510"]

    #民進党　参議院
    minshinto_ginlist=["DrSakurai","eri_line","etakashi","fuku_tetsu","hirayamasachiko","katsusikanai","KawadaOffice",
    "konishihiroyuki","kouhei1005mon","makiyama1192","masayo_tanabu","Mashiko_sangiin","MayamaMia",
    "MiekoKamimoto","Morimoto_Shinji","naokikazama","OgawaToshioMP","renho_sha","SHIMBA_OFFICE",
    "toshio_ishigami","yfujitaDPJ","yoshikawasaori"]

    sum1 = 0 #スコア
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    sum6 = 0
    sum7 = 0

    #右翼用配列
    score_uyoku_jiminto=[]#スコアリング結果を格納する配列
    score_uyoku_kibounoto=[]
    score_uyoku_koumeito=[]
    score_uyoku_minshinto=[]
    score_uyoku_nihonkyosanto=[]
    score_uyoku_nihon_isin_no_to=[]
    score_uyoku_rikkennminshuto=[]

    #左翼用配
    score_sayoku_jiminto=[]#スコアリング結果を格納する配列
    score_sayoku_kibounoto=[]
    score_sayoku_koumeito=[]
    score_sayoku_minshinto=[]
    score_sayoku_nihonkyosanto=[]
    score_sayoku_nihon_isin_no_to=[]
    score_sayoku_rikkennminshuto=[]

    #最終的スコア
    score_jiminto=[]#スコアリング結果を格納する配列
    score_kibounoto=[]
    score_koumeito=[]
    score_minshinto=[]
    score_nihonkyosanto=[]
    score_nihon_isin_no_to=[]
    score_rikkennminshuto=[]

    for a in jiminto_ginlist:#議員リストのループ
        for row in h:#データベースのループ
            if(a == row[2]):#議員リストの議員とデータベースの議員の名前が一致するか判定
                for tango in uyoku_tango:#単語辞書のループ
                    if(tango in row[3]):
                        sum1 += 1#スコアを1加算する
        score_uyoku_jiminto.append(sum1)
        sum1=0


    for a in rikkennminshuto_ginlist:#議員リストのループ
        for row in b:#データベースのループ
            if(a == row[2]):#議員リストの議員とデータベースの議員の名前が一致するか判定
                for tango in uyoku_tango:#単語辞書のループ
                    if(tango in row[3]):
                        sum2 += 1#スコアを1加算する
        score_uyoku_rikkennminshuto.append(sum2)
        sum2=0


    for a in nihonkyosanto_ginlist:#議員リストのループ
        for row in d:#データベースのループ
            if(a == row[2]):#議員リストの議員とデータベースの議員の名前が一致するか判定
                for tango in uyoku_tango:#単語辞書のループ
                    if(tango in row[3]):
                        sum3 += 1#スコアを1加算する
        score_uyoku_nihonkyosanto.append(sum3)
        sum3=0



    for a in koumeito_ginlist:#議員リストのループ
        for row in f:#データベースのループ
            if(a == row[2]):#議員リストの議員とデータベースの議員の名前が一致するか判定
                for tango in uyoku_tango:#単語辞書のループ
                    if(tango in row[3]):
                        sum4 += 1#スコアを1加算する
        score_uyoku_koumeito.append(sum4)
        sum4=0


    for a in nihon_isin_no_to_ginlist:#議員リストのループ
        for row in c:#データベースのループ
            if(a == row[2]):#議員リストの議員とデータベースの議員の名前が一致するか判定
                for tango in uyoku_tango:#単語辞書のループ
                    if(tango in row[3]):
                        sum5 += 1#スコアを1加算する
        score_uyoku_nihon_isin_no_to.append(sum5)
        sum5=0

    for a in kibounoto_ginlist:#議員リストのループ
        for row in g:#データベースのループ
            if(a == row[2]):#議員リストの議員とデータベースの議員の名前が一致するか判定
                for tango in uyoku_tango:#単語辞書のループ
                    if(tango in row[3]):
                        sum6 += 1#スコアを1加算する
        score_uyoku_kibounoto.append(sum6)
        sum6=0

    for a in minshinto_ginlist:#議員リストのループ
        for row in e:#データベースのループ
            if(a == row[2]):#議員リストの議員とデータベースの議員の名前が一致するか判定
                for tango in uyoku_tango:#単語辞書のループ
                    if(tango in row[3]):
                        sum7 += 1#スコアを1加算する
        score_uyoku_minshinto.append(sum7)
        sum7=0

    for a in jiminto_ginlist:#議員リストのループ
        for row in h:#データベースのループ
            if(a == row[2]):#議員リストの議員とデータベースの議員の名前が一致するか判定
                for tango in sayoku_tango:#単語辞書のループ
                    if(tango in row[3]):
                        sum1 += 1#スコアを1加算する
        score_sayoku_jiminto.append(sum1)
        sum1=0

    for a in rikkennminshuto_ginlist:#議員リストのループ
        for row in b:#データベースのループ
            if(a == row[2]):#議員リストの議員とデータベースの議員の名前が一致するか判定
                for tango in sayoku_tango:#単語辞書のループ
                    if(tango in row[3]):
                        sum2 += 1#スコアを1加算する
        score_sayoku_rikkennminshuto.append(sum2)
        sum2=0

    for a in nihonkyosanto_ginlist:#議員リストのループ
        for row in d:#データベースのループ
            if(a == row[2]):#議員リストの議員とデータベースの議員の名前が一致するか判定
                for tango in sayoku_tango:#単語辞書のループ
                    if(tango in row[3]):
                        sum3 += 1#スコアを1加算する
        score_sayoku_nihonkyosanto.append(sum3)
        sum3=0

    for a in koumeito_ginlist:#議員リストのループ
        for row in f:#データベースのループ
            if(a == row[2]):#議員リストの議員とデータベースの議員の名前が一致するか判定
                for tango in sayoku_tango:#単語辞書のループ
                    if(tango in row[3]):
                        sum4 += 1#スコアを1加算する
        score_sayoku_koumeito.append(sum4)
        sum4=0

    for a in nihon_isin_no_to_ginlist:#議員リストのループ
        for row in c:#データベースのループ
            if(a == row[2]):#議員リストの議員とデータベースの議員の名前が一致するか判定
                for tango in sayoku_tango:#単語辞書のループ
                    if(tango in row[3]):
                        sum5 += 1#スコアを1加算する
        score_sayoku_nihon_isin_no_to.append(sum5)
        sum5=0

    for a in kibounoto_ginlist:#議員リストのループ
        for row in g:#データベースのループ
            if(a == row[2]):#議員リストの議員とデータベースの議員の名前が一致するか判定
                for tango in sayoku_tango:#単語辞書のループ
                    if(tango in row[3]):
                        sum6 += 1#スコアを1加算する
        score_sayoku_kibounoto.append(sum6)
        sum6=0

    for a in minshinto_ginlist:#議員リストのループ
        for row in e:#データベースのループ
            if(a == row[2]):#議員リストの議員とデータベースの議員の名前が一致するか判定
                for tango in sayoku_tango:#単語辞書のループ
                    if(tango in row[3]):
                        sum7 += 1#スコアを1加算する
        score_sayoku_minshinto.append(sum7)
        sum7=0

    #自民党スコア算出
    for i in range(219):
        s = score_uyoku_jiminto[i] - score_sayoku_jiminto[i]
        score_jiminto.append(s)

    #希望の党スコア算出
    for i in range(38):
        s = score_uyoku_kibounoto[i] - score_sayoku_kibounoto[i]
        score_kibounoto.append(s)

    #公明党スコア算出
    for i in range(40):
        s = score_uyoku_koumeito[i] - score_sayoku_koumeito[i]
        score_koumeito.append(s)

    #民進党スコア算出
    for i in range(22):
        s = score_uyoku_minshinto[i] - score_sayoku_minshinto[i]
        score_minshinto.append(s)

    #日本共産党スコア算出
    for i in range(23):
        s = score_uyoku_nihonkyosanto[i] - score_sayoku_nihonkyosanto[i]
        score_nihonkyosanto.append(s)

    #日本維新の党スコア算出
    for i in range(8):
        s = score_uyoku_nihon_isin_no_to[i] - score_sayoku_nihon_isin_no_to[i]
        score_nihon_isin_no_to.append(s)

    #立憲民主党スコア算出
    for i in range(42):
        s = score_uyoku_rikkennminshuto[i] - score_sayoku_rikkennminshuto[i]
        score_rikkennminshuto.append(s)



    #, lineterminator='\n'
    with open("jiminto.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(score_jiminto)

    with open("rikkennminshuto.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(score_rikkennminshuto)

    with open("nihonkyosanto.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(score_nihonkyosanto)

    with open("nihon_isin_no_to.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(score_nihon_isin_no_to)

    with open("minshinto.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(score_minshinto)

    with open("koumeito.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(score_koumeito)

    with open("kibounoto.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(score_kibounoto)


    # データベースから切断
    cursor.close()
    connect.close()
