# Event Test Scenarios

## Event sequence testing....

### Scenario es.01

This is the first event observed for the entity and therefore there is no previous status aggregation/summary. This assumes the aggregate rules for creating one have been fulfilled.

### Scenario es.02

This is the second event observed and the events have arrived in order. The event needs to be recorded and the new aggregate calculated. This assumes the aggregate rules for creating one have been fulfilled.

### Scenario es.03

This is the third event observed and the events have arrived in order. The event needs to be recorded and the new aggregate calculated. This assumes the aggregate rules for creating one have been fulfilled.

### Scenario es.04

This is the third event observed and the events have arrived out of order. The third event recieved is actually the second event when ordered. The event needs to be recorded and the old aggregate needs removing and two new ones adding. This assumes the aggregate rules for creating one have been fulfilled.

### Scenario es.05

This is the second event observed and the events have arrived out of order. The second event recieved is actually the first event when ordered. The event needs to be recorded and the original aggregate needs removing and two new ones adding. This assumes the aggregate rules for creating one have been fulfilled.

## Event aggregation trigger testing...

### Scenario at.01

The difference between events isn't significant enough to trigger an aggregation being created. Therefore the event is recorded but no aggregation is created.

### Scenario at.02

The difference between events is significant enough to trigger an aggregation to be created. Therefore the event is recorded and an aggregation is created

## Aggregation rules are implemented...

### Scenario ar.01

The value for the significant field is lower than the previous event triggering a "reduction" aggregation.

### Scenario ar.02

The state for the significant field has moved from a to b triggering a "transition" aggregation.


