from miniPEG import PEG

# syntax from https://github.com/justinnhli/pegparse/blob/master/pegparse/peg.peg

peg_syntax1 = '''# top-level
syntax        = opt_space ( definition opt_space )*;
definition    = identifier opt_space "=" opt_space expression opt_space ";";
             
# expressions
expression    = choice;
choice        = ( "|" opt_space )? sequence ( opt_space "|" opt_space sequence )*;
sequence      = item ( req_space item )*;
item          = zero_or_more
              | zero_or_one
              | one_or_more
              | and_predicate
              | not_predicate
              | term;
zero_or_more  = term opt_space "*";
zero_or_one   = term opt_space "?";
one_or_more   = term opt_space "+";
and_predicate = "&" opt_space term;
not_predicate = "!" opt_space term;
term          = paren | atom;
paren         = "(" opt_space expression opt_space ")";

# atoms
atom          = identifier
              | builtin
              | literal;
identifier    = ( LOWER )+ ( "_" ( LOWER )+ )*;
builtin       = ( UPPER )+;
literal       = d_string
              | s_string;
d_string      = '"' ( !( '"' ) PRINT )* '"';
s_string      = "'" ( !( "'" ) PRINT )* "'";

# whitespace
opt_space     = ( space )*;
req_space     = ( space )+;
space         = "#" ( PRINT )* NEWLINE
              | BLANK
              | NEWLINE;
'''

#syntax from https://github.com/pombreda/XPEG/blob/master/xpeg/xpeg.grammar

peg_syntax2='''
# Rules
<rules>                    = rule+
<rule>                     = rule_identifier assignment expression actions?
<expression>               = sequence ("|" sequence)*
<sequence>                 = prefix*
<prefix>                   = lookahead_assertion? suffix
<suffix>                   = primary quantifier?
<primary>                  = rule_reference 
                           |  parenthesized_expression
                           |  literal
                           |  regex
<parenthesized_expression> = "(" expression ")"
<actions>                  = skip_action

# Implicit tokens
<assignment>          = "="
<rule_identifier>     = ~"<[a-z_][a-z0-9_]*>"i
<skip_action>         = ~"[skip]"i
<regex>               = ~"~u?r?\".*?[^\\]\"[ilmsux]*"is
<literal>             = ~"u?r?\".*?[^\\]\""is
<rule_reference>      = ~"[a-z_][a-z0-9_]*"i
<lookahead_assertion> = ~"[&!]"
<quantifier>          = ~"[?*+]|{[0-9]+(\s*,\s*([0-9]+)?)?}"
<comment>             = ~"#[^\r\n]*" [skip]
<spaces>              = ~"(?:\t|\s|\n)+" [skip]

'''