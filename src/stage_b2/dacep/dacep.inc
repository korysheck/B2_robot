define hokuyo ranger
(
	sensor( 			
        range [ 0.0  5.0 ] # [min max]
        fov 170 # field of view in DEGREES
        samples 180 # how many samples are there in fov?
        pose [ 0 0 0.1 0 ]
    )

	block( points 4
        point[0] [0 0]
        point[1] [0 1]
        point[2] [1 1]
        point[3] [1 0]
        z [0 0.21]
    )

    # generic model properties
    size [ 0.156 0.155 0.19 ] # dimensions from LMS200 data sheet	
    color "blue"
)

define daceps_sonar sensor
(
    # define the size of each transducer [xsize ysize zsize] in meters
    size [0.01 0.05 0.01 ] 
    # define the range bounds [min max]
    range [0.3 5.0]
    # define the angular field of view in degrees
    fov 15
	# define the number of samples spread over the fov
    samples 1
    # define the color that ranges are drawn in the gui
    color_rgba [ 0 1 0 1 ] 
)

define daceps_sonars ranger
( 
  # one line for each sonar [xpos ypos zpos heading]
  daceps_sonar( pose [ 0.5 0.5 0 30]) # left corner
  daceps_sonar( pose [ 0.5 -0.5 0 -30]) # right corner
)

define dacep position
(  
  size [1 1 0.25]          # actual size
  origin [0.25 0 0 0]   # centre of the rotation relative to the geometric
  #
  # simplified Body shape:
  block( 
	points 6
	point[0] [0.75 0]
	point[1] [1 0.25]
	point[2] [1 0.75]
	point[3] [0.75 1]
	point[4] [0 1]
	point[5] [0 0]
	z [0 1]
  )
  
  # diferencial chassis
  drive "diff"

  # report error-free position in world coordinates
  localization "gps"
  localization_origin [ 0 0 0 0 ]
  
  # sensors attached
  daceps_sonars()
  # daceps sonars will be ranger:0 and the laser will be ranger:1
  hokuyo( pose [0.75 0 0 0])
)
