;; Block A is on the table, B is on A and C on B.  A red sprayer is on
;; the table.  A green paint can is on the sprayer and a blue paint
;; can on the green paint can and a water bucket on the blue can.  A
;; clean brush is on the water bucket.  The goal is to make A red, B
;; green and C blue and to have A on B, B on C and C on the table. The
;; brush should be clean and on top of the paint can with green paint.

(define (problem 5)
	(:domain hw6)
	
	(:objects 
		;3 blocks
		block_a - Block
		block_b - Block
		block_c - Block
		
		;1 red sprayers 
		red_sprayer - Spraycan
		
		;2 paint cans...blue and green
		blue_paint_can - PaintCan
		green_paint_can - PaintCan
		
		;1 paint brush
		paint_brush - PaintBrush
		
		;1 water bucket
		water_bucket - WaterBucket
	)
  
	(:init 
		(arm-empty)
		
		; Block A is on the table, B is on A and C on B.
		(on-table block_a)
		(on block_b block_a)
		(on block_c block_b)
		(clear block_c)
		
		;red sprayer is on the table.
		(is-color red_sprayer RED)
		(on-table red_sprayer)
		
		;A green paint can is on the sprayer 
		(is-color green_paint_can GREEN)
		(on green_paint_can red_sprayer)
		
		;blue paint can is on the green paint can 
		(is-color blue_paint_can BLUE)
		(on blue_paint_can green_paint_can)
		
		;water bucket is on the blue can.  
		(on water_bucket blue_paint_can)
		
		;clean brush is on the water bucket.
		(on paint_brush water_bucket)
		(clear paint_brush)
		(clean paint_brush)
		(is-color paint_brush NONE)
		
	)
  
	(:goal 
		(and 
			;(arm-empty) 
			
			;make A red, B green and C blue 
			(looks block_a RED)
			(looks block_b GREEN)
			(looks block_c BLUE)
			
			;have A on B, B on C and C on the table. 
			(clear block_a)
			(on block_a block_b)
			(on block_b block_c)
			(on-table block_c)
			
			;The brush should be clean and on top of the paint can with green paint.
			(clean paint_brush)
			(is-color paint_brush NONE)
			(on paint_brush green_paint_can)
		)
	)
)
