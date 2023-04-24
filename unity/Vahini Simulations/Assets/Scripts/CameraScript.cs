using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraScript : MonoBehaviour
{
    private GameObject T;
    private GameObject target;
    public float speed = 1.5f;
    public int index;

    // Start is called before the first frame update
    void Start()
    {
        target = GameObject.Find("/Vehicle");
        T = GameObject.Find("/TrackingTarget");
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        this.transform.LookAt(target.transform);
        float vehicle_move = Mathf.Abs (Vector3.Distance (this.transform.position, T.transform.position) * speed);
        this.transform.position = Vector3.MoveTowards(T.transform.position, T.transform.position, vehicle_move * Time.deltaTime);
    }
}
