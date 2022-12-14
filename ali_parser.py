# ------------------------------------------------------------
# parser.py
#
# parser for ALi language
# ------------------------------------------------------------
import ply.yacc as yacc

from lexer import tokens
from semantic_rules import semantics

# ----------------------
# GLOBAL RULES 
def p_program(p):
    '''program : global_vars_funs main
               | main'''

def p_global_vars_funs(p):
    '''global_vars_funs : g_vf''' 

def p_g_vf(p):
    '''g_vf : vars functions
            | vars
            | functions'''

def p_main(p):
    '''main : FUNC MAIN found_main_function '(' ')' '{' main_block '}'  end_main_func'''

def p_found_main_function(p):
    ''' found_main_function : '''
    semantics.found_main_function()

def p_end_main_func(p):
    '''end_main_func : '''
    semantics.end_main_function()

# ----------------------
# MAIN FUNCTION RULES 
def p_main_block(p):
    '''main_block : main_block_p start_function update_function'''

# This adds the possibility of having a main function that goes straight to the start and update functions
def p_main_block_p(p):
    '''main_block_p : vars stm
                    | vars '''

def p_start_function(p):
    '''start_function : VOID FUNC START '(' ')' '{' sft '}' '''                       
    semantics.gen_start_quad()

def p_update_function(p):
    '''update_function : VOID FUNC UPDATE update_start '(' ')' interior_block update_end '''

def p_update_start(p):
    '''
    update_start : 
    '''
    semantics.update_start()

def p_update_end(p):
    '''
    update_end :
    '''
    semantics.update_end()

def p_sft(p):
    '''sft : gen_canvas gen_canvas_quad stm
           | default_gen_canvas gen_canvas_quad stm '''

def p_default_gen_canvas(p):
    '''
    default_gen_canvas :
    '''
    p[0] = False

def p_gen_canvas_quad(p):
    '''
    gen_canvas_quad :
    '''
    if p[-1]:
        # use the values from gen canvas function
        # they will be the last two in the operands stack and the last value in the constants stack
        semantics.gen_canvas(True)
    else:
        # generate canvas with default values
        semantics.gen_canvas(False)

def p_special_function_statement(p):
    '''special_function_statement : set_canvas_title
                                  | set_canvas_bg 
                                  | draw_game_object 
                                  | quit_game '''

# TODO: Add checks to make sure params are of the right type
def p_gen_canvas(p):
    '''gen_canvas : GEN_CANVAS '(' expression ',' expression ',' STRING_CONST add_const_to_operand_stack_string ')' ';' '''
    p[0] = True

def p_set_canvas_title(p):
    '''set_canvas_title : SET_CANVAS_TITLE '(' STRING_CONST add_const_to_operand_stack_string ')' ';' '''
    semantics.set_canvas_title()
    

def p_set_canvas_bg(p):
    '''set_canvas_bg : SET_CANVAS_BG '(' STRING_CONST add_const_to_operand_stack_string ')' ';' '''
    semantics.set_canvas_bg_color()

# Special getter functions will be treated as expressions 
def p_get_window_h(p):
    '''get_window_h : GET_WINDOW_H '(' ')' '''
    semantics.get_window_height()

def p_get_window_w(p):
    '''get_window_w : GET_WINDOW_W '(' ')' '''
    semantics.get_window_width()

def p_get_game_ev(p):
    '''get_game_ev : GET_GAME_EV '(' ')' '''
    semantics.get_game_event()

def p_draw_game_object(p):
    '''draw_game_object : DRAW_GAME_OBJECT '(' expression ',' expression ',' expression ',' expression ',' STRING_CONST add_const_to_operand_stack_string ')' ';' '''
    semantics.draw_game_object()

def p_quit_game(p):
    '''quit_game :  QUIT_GAME '(' ')' ';' '''
    semantics.quit_game()

# ----------------------
# STATEMENTS RULES 

def p_function_block(p):
    '''function_block : vars stm
                        | stm '''

def p_stm(p):
    '''stm : statements stm_p '''

def p_stm_p(p):
    '''stm_p : stm
             | empty'''
             
def p_vars(p):
    '''vars : VAR ids ':' vars_types ';' store_ids vars_p'''

def p_vars_types(p):
    '''vars_types : type
                  | array_type'''

def p_vars_p(p):
    '''vars_p : vars
              | empty'''

def p_ids(p):
    '''ids : ID store_id ids_p
           | ID store_id_array array_indexing_init ids_p'''

def p_store_id(p):
    '''store_id : '''
    semantics.add_id(p[-1], False)

def p_store_id_array(p):
    '''store_id_array : '''
    semantics.add_id(p[-1], True)

def p_store_ids(p):
    '''store_ids : '''
    semantics.store_ids()

def p_ids_p(p):
    '''ids_p : ',' ids
             | empty'''

def p_type(p):
    '''type : INT set_current_type
            | FLOAT set_current_type
            | CHAR set_current_type
            | BOOL set_current_type '''
    p[0] = p[1]

def p_set_current_type(p):
    '''set_current_type : '''
    semantics.set_current_type(p[-1])

def p_array_type(p):
    '''array_type : ARRAY '<' type '>' '''

def p_functions(p):
    '''functions : return_function functions
                 | void_function functions
                 | return_function
                 | void_function'''

def p_return_function(p):
    '''return_function : type FUNC ID store_function '(' p ')' store_all_params '{' start_function_ic function_block end_function '}' '''

def p_p(p):
    '''p : params
         | empty'''

def p_void_function(p):
    '''void_function : VOID set_current_type FUNC ID store_function '(' p ')' store_all_params '{' start_function_ic function_block end_function '}' '''

def p_store_function(p):
    '''store_function : '''
    semantics.store_function(p[-1])

def p_start_function_ic(p):
    '''start_function_ic : '''
    semantics.start_function()

def p_end_function(p):
    '''end_function : '''
    semantics.end_function()

def p_store_all_params(p):
    '''
    store_all_params :
    '''
    semantics.store_all_params()

def p_statements(p):
    '''statements : assignment ';'
                  | call_to_fun ';'
                  | array_init ';' 
                  | write
                  | begin_if_stm conditionals
                  | while
                  | for
                  | special_function_statement
                  | RETURN expression ';' handle_return_statement '''

def p_handle_return_statement(p):
    '''
    handle_return_statement : 
    '''
    semantics.handle_return_statement()

def p_conditionals(p):
    '''conditionals : if_statement end_if
                    | if_else_statement end_if
                    | if_else_if_statement end_if '''

def p_begin_if_stm(p):
    '''
    begin_if_stm :
    '''
    semantics.begin_if()

def p_if_statement(p):
    '''if_statement : simple_if_statement'''

def p_simple_if_statement(p):
    '''simple_if_statement : IF '(' expression ')' start_if  interior_block'''

def p_if_else_statement(p):
    '''if_else_statement : simple_if_statement simple_else_statement'''

def p_simple_else_statement(p):
    '''simple_else_statement : start_else ELSE interior_block'''

def p_if_else_if_statement(p):
    '''if_else_if_statement : simple_if_statement simple_else_if_statement simple_else_statement
                            | simple_if_statement simple_else_if_statement'''

def p_simple_else_if_statement(p):
    '''simple_else_if_statement : start_else ELIF '(' expression ')' start_if interior_block more_else_if_statement '''

def p_more_else_if_statement(p):
    '''more_else_if_statement : simple_else_if_statement
                              | empty'''

def p_start_if(p):
    '''start_if : '''
    semantics.if_start()

def p_start_else(p):
    '''start_else : '''
    semantics.else_start()

def p_end_if(p):
    '''end_if : '''
    semantics.end_if()

def p_interior_block(p):
    '''interior_block : '{' '}'
                      | '{' stm '}' '''

def p_params(p):
    '''params : ID ':' type ',' params
              | ID ':' type'''
    semantics.store_function_param(p[1], p[3])

def p_assignment(p):
    '''assignment : variable '=' add_op expression '''
    semantics.gen_assignment_quad()

def p_array_init(p):
    '''array_init : variable '=' '[' exp_1d ']'
                  | variable '=' '[' exp_2d ']' '''
    semantics.init_array(p[1])

def p_exp_1d(p):
    '''exp_1d : expression ',' exp_1d
              | expression'''

def p_exp_2d(p):
    '''exp_2d : '[' exp_1d  ']' ',' exp_2d
              | '[' exp_1d ']' '''

def p_write(p):
    '''write : PRINT '(' write_p ')' ';'
             | PRINT '(' write_p ')' '<' '<' ENDL  ';' '''
    if len(p) - 1 == 8: 
        semantics.end_print()
 
def p_write_p(p):
    '''write_p : write_param ',' write_p 
               | write_param '''

def p_write_param(p):
    '''write_param : STRING_CONST add_const_to_operand_stack_string print_value
                   | variable print_value'''

def p_print_value(p):
    '''
    print_value :
    '''
    semantics.print_value()


def p_call_to_fun(p):
    '''call_to_fun : ID verify_function '(' gen_activation_quad ')' verify_params_number end_function_call
                   | ID verify_function '(' gen_activation_quad call_p ')' verify_params_number end_function_call '''

def p_call_p(p):
    '''call_p : expression call_argument ',' move_to_next_param  call_p
              | expression call_argument '''

def p_verify_function(p):
    ''' verify_function : '''
    semantics.verify_function(p[-1])

def p_gen_activation_quad(p):
    ''' gen_activation_quad : '''
    semantics.gen_activation_record_quad()

def p_call_argument(p):
    ''' call_argument : '''
    semantics.call_argument()

def p_move_to_next_param(p):
    ''' move_to_next_param : '''
    semantics.move_to_next_param()

def p_verify_params_number(p):
    ''' verify_params_number : '''
    semantics.verify_params_number()

def p_end_function_call(p):
    ''' end_function_call : '''
    semantics.end_function_call()

def p_array_indexing(p):
    '''array_indexing : ID '[' expression ']'
                      | ID '[' expression ']'  '[' expression ']' '''
    if len(p)-1 == 4:
        semantics.gen_array_indexing_quads(p[1], 1)
    else:
        semantics.gen_array_indexing_quads(p[1], 2)

def p_array_indexing_init(p):
    '''array_indexing_init : '[' I_CONST set_dim1_size ']'
                           | '[' I_CONST set_dim1_size ']'  '[' I_CONST set_dim2_size ']' '''

def p_set_dim1_size(p):
    ''' set_dim1_size : '''
    semantics.set_dim1_size(p[-1])

def p_set_dim2_size(p):
    ''' set_dim2_size : '''
    semantics.set_dim2_size(p[-1])

def p_while(p):
    '''while : WHILE start_while '(' expression ')' evaluate_while_expression interior_block end_while'''

def p_start_while(p):
    '''
    start_while :
    '''
    semantics.start_while()

def p_evaluate_while_expression(p):
    '''
    evaluate_while_expression :
    '''
    semantics.evaluate_while_expression()

def p_end_while(p):
    '''
    end_while :
    '''
    semantics.end_while()

def p_for(p):
    '''for : FOR '(' assignment ';' start_for expression ';' eval_for_expression assignment save_for_increment ')' interior_block end_for'''

def p_start_for(p):
    '''
    start_for :
    '''
    semantics.start_for()

def p_eval_for_expression(p):
    '''
    eval_for_expression :
    '''
    semantics.evaluate_for_expression()

def p_end_for(p):
    '''
    end_for :
    '''
    semantics.end_for()

def p_save_for_increment(p):
    '''
    save_for_increment : 
    '''
    semantics.save_for_increment()

# ----------------------
# EXRPESSIONS RULES 

def p_expression(p):
    '''expression : t_exp 
                  | t_exp OR add_op expression gen_operation'''

def p_t_exp(p):
    '''t_exp : g_exp 
             | g_exp AND add_op t_exp gen_operation'''

def p_g_exp(p):
    '''g_exp : m_exp 
          | m_exp op g_exp gen_operation
          | '!' add_op g_exp not_action'''

def p_not_action(p):
    '''
    not_action : 
    '''
    semantics.not_quad()

def p_op(p):
    '''op : '>' add_op
          | '<' add_op
          | GREATER_EQ add_op
          | LESS_EQ add_op
          | EQUAL add_op
          | DIFFERENT add_op'''

def p_m_exp(p):
    '''m_exp : term
           | m_exp '+' add_op term gen_operation
           | m_exp '-' add_op term gen_operation '''

def p_term(p):
    '''term : factor
            | term '*' add_op factor gen_operation
            | term '/' add_op factor gen_operation'''

def p_add_op(p):
    '''
    add_op :
    '''
    semantics.add_operator(p[-1])

def p_factor(p):
    '''factor : '(' expression ')'
              | constants '''

def p_constants(p):
    '''constants : I_CONST add_const_to_operand_stack_int
                 | F_CONST add_const_to_operand_stack_float
                 | C_CONST add_const_to_operand_stack_char
                 | TRUE add_const_to_operand_stack_bool
                 | FALSE add_const_to_operand_stack_bool
                 | variable
                 | call_to_fun
                 | get_window_h
                 | get_window_w
                 | get_game_ev'''

def p_variable(p):
    '''variable : array_indexing 
                | ID'''
    if p[1] is not None:
        semantics.add_id_operand(p[1])
    p[0] = p[1]


def p_add_const_to_operand_stack_string(p):
    '''
    add_const_to_operand_stack_string : 
    '''
    semantics.add_constant_operand(p[-1], 'string')

def p_add_const_to_operand_stack_int(p):
    '''add_const_to_operand_stack_int : '''
    semantics.add_constant_operand(p[-1], 'int')

def p_add_const_to_operand_stack_float(p):
    '''add_const_to_operand_stack_float : '''
    semantics.add_constant_operand(p[-1], 'float')

def p_add_const_to_operand_stack_char(p):
    '''add_const_to_operand_stack_char : '''
    semantics.add_constant_operand(p[-1], 'char')

def p_gen_operation(p):
    ''' gen_operation : '''
    semantics.gen_operation_quad()

def p_add_const_to_operand_stack_bool(p):
    '''add_const_to_operand_stack_bool : '''
    semantics.add_constant_operand(p[-1], 'bool')


# ----------------------
# EMPTY & ERROR RULES 
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    err_string = f"Syntax error in input at line {p.lineno} at character {p.lexpos} unexpected \'{p.value}\' "
    raise Exception(err_string)

ali_parser = yacc.yacc(debug=True)

def test():
    print('Enter file name to be tested (with .al extension)')
    filename = input()
    file = open(filename)
    input_str = file.read()
    file.close()
    ali_parser.parse(input_str) 
    print('Accepted code')

if __name__ == "__main__":
    test()
    print(semantics.id_queue)
    print(semantics.types_stack)
    print(semantics.operands_stack)
    print(semantics.operators_stack)
    print(semantics.const_vars_table)
    print(semantics.function_directory)
    i = 0
    for quad in semantics.quadruples:
        print(f'{i}. {quad}')
        i += 1