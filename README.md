
#### Repo Leírás:
A repository a NAV elektronikus árverési felületén található ingóság árverések tételeinek scrapelésére szolgáló python scriptet tartalmaz.  
A függőségek telepítése után a script paraméterek nélkül futtatható a shellből.  
A script az EÁF [tételek oldaláról](https://arveres.nav.gov.hu/index-meghirdetesek-ingosag.html?.actionId=action.auction.FilterAction&fi=kategoriaFilter&fk=auctionFilterData_1&v=-1&FRAME_SKIP_DEJAVU=1) leszedi az összes fenn található tételt és egy táblázatot készít, melyet csv formátumban lement az OUTDIR változóban tárolt elérési útvonalra.

A táblázat oszlopsémája:   
* auction_id: Árverés rövid sorszáma (Pl.: 233397), adattípus: integer  
* item_type: Kategória, adattípus: string  
* item_name: Árverezett tétel, adattípus: string   
* price: Becsérték, adattípus: integer  
* posted_on: Meghirdetés dátum, adattípus: datetime   	  
* begins_at: Kezdési dátum és idő, adattípus: datetime  	  
* ends_at: Befejezési dátum és idő, adattípus: datetime   
* contact_tel: Kontakt telefon, adattípus: string	  
* auction_id_long:  Árverés teljes sorszáma (Pl.: 233397/210414), adattípus: string  
* item_ur: tétel abszolút url címe, adattípus: string  

A kimenet fileból pár példa csv az [Examples](https://github.com/xngst/NAV-ingosag-arveres-scraper/tree/master/Examples) mappában található.

#### Az árverési felületről:
##### [NAV EÁF honlap](https://arveres.nav.gov.hu/index-fooldal-ingosag.html?.actionId=action.common.ActivateItemAction:1619340077560&item=mainPage)

Az Elektronikus Árverési Felület (EÁF) olyan virtuális árverési csarnok, ahol a NAV végrehajtási eljárásai során lefoglalt és a NAV birtokában lévő ingóságok és ingatlanok árverése történik.

Az árverésen résztvevők - ideértve annak nyertesét is - az árverés befejezéséig anonim módon árvereznek. Árverési vevő lehet bárki, aki regisztrálta magát az Ügyfélkapun és az árverés szabályait elfogadja. Egy árverési tételre vonatkozó árverés az árverés kezdődátumtól a végdátumig tart, ez alatt kell az ajánlatokat megtenni. Az árverés nyertese az árverési vételár fejében az illetékes adóigazgatóságnál veheti át az ingóságot. Ingatlan árverés esetén a részvétel előfeltétele a hirdetményben szereplő előleg megfizetése átutalás útján az árverés kezdetéig. 
