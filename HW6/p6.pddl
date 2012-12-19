;; Block A is on the table, B is on A and C on B.  Cans of red, green
;; and blue paint are on the table along with three clean brushes.
;; There is no water bucket.  The goal is to make A red, B green and C
;; blue and to have A on B, B on C and C on the table and the arm
;; empty.

(define (problem 6)
	(:domain hw6)
  
	(:objects
		;3 blocks
		block_a - Block
		block_b - Block
		block_c - Block
		
		;3 paint cans...RGB
		red_paint_can - PaintCan
		green_paint_can - PaintCan
		blue_paint_can - PaintCan
		
		;3 paint brushes
		paint_brush_1 - PaintBrush
		paint_brush_2 - PaintBrush
		paint_brush_3 - PaintBrush
	)
  
	(:init 
		(arm-empty) 
		
		; Block A is on the table, B is on A and C on B.
		(on-table block_a)
		(on block_b block_a)
		(on block_c block_b)
		(clear block_c)
		
		;Cans of red, green and blue paint are on the table 
		;along with three clean brushes.
		(is-color red_paint_can RED)
		(on-table red_paint_can)
		(clear red_paint_can)
		
		(is-color blue_paint_can BLUE)
		(on-table blue_paint_can)
		(clear blue_paint_can)
		
		(is-color green_paint_can GREEN)
		(on-table green_paint_can)
		(clear green_paint_can)
		
		(clean paint_brush_1)
		(is-color paint_brush_1 NONE)
		(on-table paint_brush_1)
		(clear paint_brush_1)
		
		(clean paint_brush_2)
		(is-color paint_brush_2 NONE)
		(on-table paint_brush_2)
		(clear paint_brush_2)
		
		(clean paint_brush_3)
		(is-color paint_brush_3 NONE)
		(on-table paint_brush_3)
		(clear paint_brush_3)
	)
	
	(:goal 
		(and 
			;the arm empty.
			(arm-empty)

			;make A red, B green and C blue 
			(looks block_a RED)
			(looks block_b GREEN)
			(looks block_c BLUE)
			
			;have A on B, B on C and C on the table
			(clear block_a)
			(on block_a block_b)
			(on block_b block_c)
			(on-table block_c)
		)
	)
)
