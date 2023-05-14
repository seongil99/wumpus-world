# AI Project: Wumpus World

## 에이전트가 처한 환경

탐험하는 에이전트가 처한 환경은 4×4 격자로 구성되어 있으며, (1,1) 격자는 안전하다(safe)고 가정한다. 4×4 격자 세계(Grid World)의 고정된 위치에 금 (gold), wumpus 괴물 및 웅덩이(pitch)가 존재한다. wumpus 괴물 및 웅덩이 가 발생할 확률은 각각의 격자에서 독립적이며, 0.10으로 가정한다. 에이전트 가 금을 획득하여 [1,1] 격자로 되돌아오면 탐험은 종료된다.

## 에이전트의 센서 입력

[ Stench, Breeze, Glitter, Bump, Scream ]

## 에이전트가 취할 수 있는 행동

[ GoForward, TurnLeft, TurnRight, Grab, Shoot, Climb ]

## 에이전트의 기본값

에이전트는 안전한 (1,1) 격자에서 출발한다. 즉, (1,1) 격자에는 wumpus 괴 물과 웅덩이가 존재하지 않으며, 금 역시 존재하지 않는다. 에이전트는 처음에 동쪽(East)을 향하고 있으며, 화살을 총 2개 가지고 있다.
