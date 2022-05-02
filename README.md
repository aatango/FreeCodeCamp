## Responsive Web Design
[FCC link](https://www.freecodecamp.org/learn/responsive-web-design/)

Unfinished certification.

## JavaScript Algorithms and Data Structures
[FCC link](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/)

Course projects done through FCC webpage. The files in this branch serve as backup.


## Data Visualisation
[FCC link](https://www.freecodecamp.org/learn/data-visualization/)

### Design decisions
Set internal challenge to finish full course within one month.

To achieve a viable product within the time frame, the following was decided:
* Aesthetic template would be maintaned across all projects. Once the design was defined in the earlier, and easier, programs, it would then be possible to alot more time to design the latter systems.
* Anything that wasn't an explicit requirement of the user stories, would be de prioritised, and might not end up being implemented (this is how the [Tree Map project](https://aatango.github.io/FreeCodeCamp/04-data-visualization/D3_Treemap.html) ended up without leaf labels).

Once it became clear the initial deadline would not be respected, priority changed; from finishing course within a month, to maintain a consistent product between all projects. 

_In the end, it would take about 1.5 months do finish the assignments._

### Tooltip testing problems
Tooltip, as presented in the [course's lesson](https://www.freecodecamp.org/learn/data-visualization/data-visualization-with-d3/add-a-tooltip-to-a-d3-element), appears not to fulfill the applicable tests:

```javascript
	[...].append('title').attr('id', 'tooltip').text([...])
```

Adapted instead method used in an [example project](https://codepen.io/freeCodeCamp/pen/GrZVaM):

```javascript
tooltip = d3.select('graph').append('div').style('visibility', 'hidden')
--snip--
d3.select('svg')
	.on('mouseover', () => tooltip.style('visibility', 'visible'))
	.on('mouseout', () => tooltip.style('visibility', 'hidden'));
```

## Scientific Computing with Python
[FCC link](https://www.freecodecamp.org/learn/scientific-computing-with-python/)

Course projects done through Replit.com, as requested in the course page. The files in this branch serve as a backup.

## Coding Interview Prep
[FCC link](https://www.freecodecamp.org/learn/coding-interview-prep/)

