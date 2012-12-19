;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Prodigy blocks world
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (domain hw6)
	(:requirements :strips :equality :typing)	
	(:constants RED - Color GREEN - Color BLUE - Color NONE - Color)
	(:types Color Block Spraycan PaintCan PaintBrush WaterBucket)
	(:predicates (on ?x ?y)
	       (on-table ?x)
	       (clear ?x)
	       (arm-empty)
	       (holding ?x)
		   
		   
		   ;applies to paint cans, paint sprays and  brushes pertaining to 
		   ;what color it contains or can paint
		   (is-color ?obj ?color - Color)
		   
		   ;exterior appearnace in terms of color
		   (looks ?obj ?color - Color)
		   
		   (clean ?paintBrush - PaintBrush)		   
	)
	
	(:action pick-up
	    :parameters (?ob1)
	    :precondition (and (clear ?ob1) (on-table ?ob1) (arm-empty))
	    :effect
			(and 
				(not (on-table ?ob1))
				(not (clear ?ob1))
				(not (arm-empty))
				(holding ?ob1)
			)
	)
  
  (:action put-down
	     :parameters (?ob)
	     :precondition (holding ?ob)
	     :effect
	     (and (not (holding ?ob))
		   (clear ?ob)
		   (arm-empty)
		   (on-table ?ob)))
	
	(:action stack
	     :parameters (?sob ?sunderob)
	     :precondition (and (holding ?sob) (clear ?sunderob))
	     :effect
		(and (not (holding ?sob))
		   (not (clear ?sunderob))
		   (clear ?sob)
		   (arm-empty)
		   (on ?sob ?sunderob)
		)
	)
	
	(:action unstack
	     :parameters (?sob ?sunderob)
	     :precondition (and (on ?sob ?sunderob) (clear ?sob) (arm-empty))
	     :effect
	     (and (holding ?sob)
		   (clear ?sunderob)
		   (not (clear ?sob))
		   (not (arm-empty))
		   (not (on ?sob ?sunderob))
		 )
	)

	(:action clean_paint_brush
		:parameters(
			?paintBrush - PaintBrush 
			?color - Color
			?waterBucket - WaterBucket
		)
		:precondition 
			(and 
				(holding ?paintBrush) 
				(not (clean ?paintBrush))
				(is-color ?paintBrush ?color)
				(on-table ?waterBucket)
				(clear ?waterBucket)
			)
		:effect
			(and
				(clean ?paintBrush)
				(is-color ?paintBrush NONE)
				(not (is-color ?paintBrush ?color))
			)
	)
	
	(:action load_paint_brush 
		:parameters (
			?paintBrush - PaintBrush 
			?color - Color
			?paintCan - PaintCan
		)
	    :precondition (and 
				(holding ?paintBrush) 
				(clean ?paintBrush)
				(is-color ?paintBrush NONE)
				
				(on-table ?paintCan)
				(clear ?paintCan) 
				(is-color ?paintCan ?color)
			)
	    :effect
			(and
				(not (clean ?paintBrush))
				(is-color ?paintBrush ?color)
				(not (is-color ?paintBrush NONE))
			)
	)
	
	(:action paint_with_brush
		:parameters(
			?obj - Block
			?paintBrush - PaintBrush
			?color - Color
		)
		:precondition 
			(and
				(holding ?paintBrush)
				(not (clean ?paintBrush))
				(is-color ?paintBrush ?color)
				(on-table ?obj)
				(clear ?obj)
			)
		:effect
			
				(looks ?obj ?color)
				(is-color ?paintBrush ?color)
				
			
	)
	
	(:action spray_paint
		:parameters(
			?obj - Block
			?sprayCan - Spraycan
			?color - Color
		)
		:precondition 
			(and
				(holding ?sprayCan)
				(is-color ?sprayCan ?color)
				
				(on-table ?obj)
				(clear ?obj)
			)
		:effect
			
				(looks ?obj ?color)
			
	)
	
)

