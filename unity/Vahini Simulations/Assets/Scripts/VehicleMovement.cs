using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;


public class VehicleMovement : MonoBehaviour
{
    private NavMeshAgent agent;
    [SerializeField]
    private Transform movePositionTransform;

    [Header("Sensors")]
    public float sensorLength = 3f;
    private float frontSensorOffsetz = 1.51f;
    private float frontSensorOffsety = 0.23f;

    public float frontSideSensorOffsetx = 0.43f;
    public float frontSideSensorAngle = 30f;



    // Start is called before the first frame update
    void Start()
    {
        
    }

    private void Awake()
    {
        agent = GetComponent<NavMeshAgent>();
    }

    // Update is called once per frame
    void Update()
    {
        // agent.destination = movePositionTransform.position;
        Sensors();
        
    }

    private void Sensors(){
        RaycastHit hit;
        Vector3 sensorStartPos = transform.position;
        sensorStartPos += transform.forward * frontSensorOffsetz;
        sensorStartPos += transform.up * frontSensorOffsety;

        // Front Sesnor
        if (Physics.Raycast(sensorStartPos, transform.forward, out hit, sensorLength))
        {
            Debug.DrawLine(sensorStartPos, hit.point);
        }
        // Front side right sensor
        sensorStartPos += transform.right * frontSideSensorOffsetx;
        if (Physics.Raycast(sensorStartPos, transform.forward, out hit, sensorLength))
        {
            Debug.DrawLine(sensorStartPos, hit.point);
        }
        // Front Right Angle Sensor
        if (Physics.Raycast(sensorStartPos, Quaternion.AngleAxis(frontSideSensorAngle, transform.up) * transform.forward, out hit, sensorLength))
        {
            Debug.DrawLine(sensorStartPos, hit.point);
        }
        // Front side left sensor
        sensorStartPos -= transform.right * 2 * frontSideSensorOffsetx;
        if (Physics.Raycast(sensorStartPos, transform.forward, out hit, sensorLength))
        {
            Debug.DrawLine(sensorStartPos, hit.point);
        }
        // Front Left Angle Sensor
        if (Physics.Raycast(sensorStartPos, Quaternion.AngleAxis(-frontSideSensorAngle, transform.up) * transform.forward, out hit, sensorLength))
        {
            Debug.DrawLine(sensorStartPos, hit.point);
        }
        

    }
}
