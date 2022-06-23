extends RigidBody2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


var speed_vector = Vector2()
var speed_length = 2

var thrust = 4

const GRAVITY = 10

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

func _integrate_forces(state):
	speed_vector.x = 0
#	speed_vector.y += GRAVITY
	var angle = self.transform.get_rotation()
	print(angle)
	if Input.is_action_pressed("ui_left"):
		add_torque(-10)
		
		
	if Input.is_action_pressed("ui_right"):
		add_torque(10)
	
	if Input.is_action_pressed("ui_accept"):
		
		apply_central_impulse(Vector2(thrust * sin(angle), -thrust*cos(angle))) 
