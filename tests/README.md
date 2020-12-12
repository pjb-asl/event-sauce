# Event Test Scenarios

## Event change identification testing...a.k.a Sequencing

### Scenario ec.01

The new event is confirmed as different to the previous event

### Scenario ec.02

The new event is confirmed as the same as the previous event

### Scenario ec.03

The next event is confirmed as being the same as the new event

## Event order testing...

### Scenario eo.01

The previous event (compared to the supplied event) is retrieved from the events list

## Event sequence testing....

### Scenario es.01

This is the first event observed for the entity and therefore needs to be recorded.

### Scenario es.02

This is the second event observed and the events have arrived in order. The event needs to be recorded. 

### Scenario es.03

This is the third event observed and the events have arrived in order. The event needs to be recorded.

### Scenario es.04

This is the third event observed and the events have arrived out of order. The third event recieved is actually the second event when ordered. The event needs to be recorded.

### Scenario es.05

This is the second event observed and the events have arrived out of order. The second event recieved is actually the first event when ordered. The event needs to be recorded.

### Scenario es.06

This is the third event observed and the events have arrived out of order. The third event recieved is actually the second event when ordered. The event needs to be recorded. The third event in the sorted list isn't different to the second and therefore needs to be deleted.

## Event aggregation trigger testing...a.k.a. Summarising - TODO!!!!

### Scenario at.01

The difference between events isn't significant enough to trigger an aggregation being created. Therefore the event is recorded but no aggregation is created.

### Scenario at.02

The difference between events is significant enough to trigger an aggregation to be created. Therefore the event is recorded and an aggregation is created

## Aggregation rules are implemented...

### Scenario ar.01

The value for the significant field is lower than the previous event triggering a "reduction" aggregation.

### Scenario ar.02

The state for the significant field has moved from a to b triggering a "transition" aggregation.


