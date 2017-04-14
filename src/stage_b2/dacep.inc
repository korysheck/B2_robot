
define hokuyo ranger
(
	sensor( 			
        range [ 0.0  5.0 ] # [min max]
        fov 170 # field of view in DEGREES
        samples 180 # how many samples are there in fov?
        pose [ 0.09 0.0 0.11 0.0 ] # pose of sensor on device body defined by "block"
    )

	block( points 4
        point[0] [0 0]
        point[1] [0.180 0]
        point[2] [0.180 0.155]
        point[3] [0 0.155]
        z [0 0.22]
    )

    # generic model properties
    size [ 0.180 0.155 0.220 ] # dimensions from dacep.urdf, tohle omezuje model block points	
    color "green"
)

define b2_cam camera
(
  # laser properties
  resolution [ 640 480 ]
  range [ 0.3 8.0 ]
  fov [ 40.0 40.0 ]
  pantilt [ 0.0 0.0 ]

  # model properties
  size [ 0.1 0.07 0.05 ]
  color "black"
  watts 100.0 # TODO find watts for sony pan-tilt camera
)


define daceps_sonar sensor
(
    # define the size of each transducer [xsize ysize zsize] in meters
    size [0.05 0.05 0.05 ]
    # define the range bounds [min max]
    range [0.3 5.0]
    # define the angular field of view in degrees
    fov 15
    # define the number of samples spread over the fov
    samples 1
    # define the color that ranges are drawn in the gui
    color "blue"
)

define daceps_sonar5 ranger
( 
  # one line for each sonar [xpos ypos zpos heading]
  daceps_sonar( pose [ 0.475 0.155 -0.5225 45]) # front left corner od originu a od vrchu body shape
)
define daceps_sonar4 ranger
( 
  daceps_sonar( pose [ 0.475 0.00 -0.5225 0]) # front middle (0.18 + 0.31)=0.49 (1.04-0.15)=0.89
)
define daceps_sonar3 ranger
( 
  daceps_sonar( pose [ 0.475 -0.155 -0.5225 -45]) # front right corner (0.18 + 0.31)
)
define daceps_sonar2 ranger
( 
  daceps_sonar( pose [ 0.1875 -0.155 -0.5225 -90]) # right middle
)
define daceps_sonar6 ranger
( 
  daceps_sonar( pose [ 0.1875 0.155 -0.5225 90]) # left middle
)
define daceps_sonar7 ranger
( 
  daceps_sonar( pose [ -0.1 0.155 -0.5225 135]) # rear left corner
)
define daceps_sonar1 ranger
( 
  daceps_sonar( pose [ -0.1 -0.155 -0.5225 -135]) # rear right corner
)

define dacep position
(  
  size [0.575 0.310 0.648] # actual size
  
  wheelbase 0.392 # rozvor kol 

# 0.18 centre of the rotation relative to the GEOMETRIC CENTRE <-x ^y, odtud se pocitaji pozice sonaru
# vytocim-li kola o 1.57 rad, toci se mi car-like podvozek okolo tohoto bodu
  origin [0.1875 0 0 0]

  # simplified Body shape:
  block( 
	points 4
	point[0] [0.575 0] # vsechno musi smerovat v ose x! - prvni souradnice
	point[1] [0.575 0.310]
	point[2] [0 0.310]
	point[3] [0 0]
	z [0 0.184]
  )
  
  block( 
	points 4
	point[0] [0.299 0.1495]
	point[1] [0.299 0.1625]
	point[2] [0.286 0.1625]
	point[3] [0.286 0.1495]
	z [0 0.648]
  )
  color "yellow"
  
  # ackermann chassis
  drive "car"
  
  # init velocity - nefunguje mi
  velocity [ 0.0 0.0 0.0 0.0 ]
  
  # [ xmin xmax ymin ymax zmin zmax amin amax ], zpomali nataceni robota, ale neomezi nataceni kol				
  velocity_bounds [-0.2 0.4 -0 0 -0 0 -30 30]					
  acceleration_bounds [-0.5 0.5 -0 0 -0 0 -30 30]

  # report error-free position in world coordinates
  localization "gps"
  localization_origin [ 0 0 0 0 ]
  

  # daceps sonars will be ranger:1,2..,6 and the laser will be ranger:0
  hokuyo( pose [0.289 0.0 -0.464 0.0]) # /base_scan_0
  
  # sensors attached
  daceps_sonar1() #/base_scan_1
  daceps_sonar2() #/base_scan_2
  daceps_sonar3() #/base_scan_3
  daceps_sonar4() #/base_scan_4
  daceps_sonar5() #/base_scan_5
  daceps_sonar6() #/base_scan_6
  daceps_sonar7() #/base_scan_7
  
  # cam attached
  b2_cam( pose [0.1925 0.0 0.0 0.0] )
)
