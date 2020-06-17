--select * from bods where  item like "%war axe%" and material = "Iron" /*and (complete < needed)*/ order by largeInd
--select * from bods where item in (select item from bods where largeInd = 8) and needed = 10
--select * from bods where largeInd = 8

select b1.item, b1.material, b1.quality, b1.largeInd, b1.needed, b2.needed, b1.id, b2.id from bods b1
left outer join bods b2 on
      b1.item = b2.item AND
	  b1.quality = b2.quality AND
	  b1.material = b2.material AND
	  b1.needed = b2.needed
WHERE
      b1.largeInd != -1 AND
	  b2.largeInd = -1
order by
      b1.largeInd ASC
--select item, quality, material, needed from bods where largeInd = -1