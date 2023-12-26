from graphviz import Digraph


def generate_NFA_graph(nfa, filename):
    dot = Digraph()
    dot.attr('node', shape='circle')
    dot.graph_attr['rankdir'] = 'LR'

    # Add nodes
    for state in nfa['states']:
        if state in nfa['final_states']:
            dot.node(state, shape='doublecircle')  # Mark final states differently
        else:
            dot.node(state)

    # Add edges
    for state, transitions in nfa['transitions'].items():
        for symbol, next_state in transitions.items():
            if state == nfa['initial_state']:
                dot.edge(state, next_state, label=symbol, arrowhead='normal')
            else:
                dot.edge(state, next_state, label=symbol)
    # Render the Digraph
    dot.render(filename, format='png')

NFA ={
        'states': {'Idle', 'Waiting', 'Refunding', 'Dispensing'},
        'input_symbols': {'Refilled', 'Amount In', 'Insufficient Money', 'Insert More', 'Out of Stock', 'Enough Money', 'Cancel',
                          'No Refund', 'Completed'},
        'transitions': {
           'Idle': {'Refilled': {'Idle'}, "Amount In": {"Waiting"}},
           'Waiting': {'Insufficient Money': {'Waiting'}, 'Insert More': {'Waiting'}, 'Out of Stock': {'Waiting'},
                 'Enough Money': {'Dispensing'}, 'Cancel': {'Refunding'}},
           'Refunding': {'Completed': {'Idle'}},
           'Dispensing': {'Completed': {'Refunding'}, 'No Refund': {'Idle'}},
    },

        'initial_state': 'Idle',
        'final_states': {'Idle'},
    }
nfaa = [NFA]
for index, nfa in enumerate(nfaa):
 filename = f'nfa_graph_{index}'
 generate_NFA_graph(nfa, filename)
