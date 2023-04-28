using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;


public class VehicleMovement : MonoBehaviour
{
    public Transform path;
    private List<Transform> nodes = new List<Transform>();
    private int currentNode = 0;
    public float maxSteerAngle = 45.0f;
    public WheelCollider wheelFL;
    public WheelCollider wheelFR;
    public WheelCollider wheelBL;
    public WheelCollider wheelBR;
    public float maxMotorTorque = 80.0f;

    private float currentSpeed;
    public float maxSpeed = 80.0f;

    // private NavMeshAgent agent;
    //[SerializeField]
    //private Transform movePositionTransform;

    [Header("Sensors")]
    public float sensorLength = 3f;
    private float frontSensorOffsetz = 1.51f;
    private float frontSensorOffsety = 0.23f;

    public float frontSideSensorOffsetx = 0.43f;
    public float frontSideSensorAngle = 30f;
    float avoidMultiplier = 0f;


    private bool avoiding = false;



    // Start is called before the first frame update
    private void Start()
    {
        Transform[] pathTransforms = path.GetComponentsInChildren<Transform>();
        nodes = new List<Transform>();
        for(int i=0;i< pathTransforms.Length; i++){
            if(pathTransforms[i] != path.transform){
                nodes.Add(pathTransforms[i]);
            } 
        }   
    }

    private void Awake()
    {
        // agent = GetComponent<NavMeshAgent>();
    }

    // Update is called once per frame
    private void FixedUpdate()
    {
        // agent.destination = movePositionTransform.position;
        ApplySteer();
        Drive();
        CheckWayPointDistance();
        Sensors();
    }

    private void Drive()
    {
        currentSpeed = 2 * Mathf.PI * wheelBL.radius * wheelBL.rpm * 60/1000;
        if (currentSpeed < maxSpeed){
            wheelBL.motorTorque = maxMotorTorque;
            wheelBL.motorTorque = maxMotorTorque;
        }
        else{
            wheelBL.motorTorque = 0.0f;
            wheelBL.motorTorque = 0.0f;
        }
        
    }

    private void ApplySteer()
    {
        Vector3 relativeVector = transform.InverseTransformPoint(nodes[currentNode].position);
        float newSteer = (relativeVector.x / relativeVector.magnitude) * maxSteerAngle;
        wheelFL.steerAngle = newSteer;
        wheelFR.steerAngle = newSteer;

    }

    private void CheckWayPointDistance()
    {
        
        if (Vector3.Distance(transform.position, nodes[currentNode].position) < 3.0f){
            if ( currentNode == nodes.Count-1){
                // Stop the vehicle
                // TODO::Remove this
                currentNode = 0;
            }
            else{
                currentNode++;
            }
            Debug.Log(currentNode);
        }
    }

    private void Sensors(){
        RaycastHit hit;
        Vector3 sensorStartPos = transform.position;
        sensorStartPos += transform.forward * frontSensorOffsetz;
        sensorStartPos += transform.up * frontSensorOffsety;
        avoiding = false;

        // Front Sesnor
        if (Physics.Raycast(sensorStartPos, transform.forward, out hit, sensorLength))
        {
            if(hit.collider.CompareTag("Terrain"))
            {
                Debug.DrawLine(sensorStartPos, hit.point);
                avoiding = true;
            }
            
        }
        // Front side right sensor
        sensorStartPos += transform.right * frontSideSensorOffsetx;
        if (Physics.Raycast(sensorStartPos, transform.forward, out hit, sensorLength))
        {
            if(hit.collider.CompareTag("Terrain"))
            {
                Debug.DrawLine(sensorStartPos, hit.point);
                avoiding = true;
                avoidMultiplier -= 1f;
                
            }
        }
        // Front Right Angle Sensor
        else if (Physics.Raycast(sensorStartPos, Quaternion.AngleAxis(frontSideSensorAngle, transform.up) * transform.forward, out hit, sensorLength))
        {
            if(hit.collider.CompareTag("Terrain"))
            {
                Debug.DrawLine(sensorStartPos, hit.point);
                avoiding = true;
                avoidMultiplier -= 0.5f;
            }
        }
        // Front side left sensor
        sensorStartPos -= transform.right * 2 * frontSideSensorOffsetx;
        if (Physics.Raycast(sensorStartPos, transform.forward, out hit, sensorLength))
        {
            if(hit.collider.CompareTag("Terrain"))
            {
                Debug.DrawLine(sensorStartPos, hit.point);
                avoiding = true;
                avoidMultiplier += 1f;
            }
        }
        // Front Left Angle Sensor
        if (Physics.Raycast(sensorStartPos, Quaternion.AngleAxis(-frontSideSensorAngle, transform.up) * transform.forward, out hit, sensorLength))
        {
            if(hit.collider.CompareTag("Terrain"))
            {
                Debug.DrawLine(sensorStartPos, hit.point);
                avoiding = true;
                avoidMultiplier += 0.5f;
            }
        }
    }
}
