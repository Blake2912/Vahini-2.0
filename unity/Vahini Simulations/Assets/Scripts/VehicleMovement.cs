using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;


public class VehicleMovement : MonoBehaviour
{
    private NavMeshAgent agent;
    [SerializeField]
    private Transform movePositionTransform;

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
        agent.destination = movePositionTransform.position;
    }
}
