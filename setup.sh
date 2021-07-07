mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"poojitha.kaperla@svce.edu.in\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
