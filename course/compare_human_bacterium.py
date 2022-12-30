global file18s_human, file16s_bacterium, count, nucleotides

def read_file(file_name: str) -> str:
    try:
        with open(file_name, 'r', encoding='utf8') as f: 
            return f.read()
    except Exception:
        raise Exception('Exception while reading the file')

def generate_dinucleodites() -> None:
    for nucleotide_i in nucleotides:
        for nucleotide_j in nucleotides: 
            count[nucleotide_i + nucleotide_j] = 0 

def write_file(file_name: str, content: str) -> str:
    try:
        c = 1
        with open(file_name, 'w', encoding='utf8') as file: 
            for i in count: 
                transparence = count[i]/max(count.values())
                file.write(content + str(transparence) + "')>" + i + "</div>")

                if(c % 4 == 0):
                    file.write("<div style='clear:both'></div>")

                c+=1
        return file
    except Exception:
        raise Exception('Exception while reading the file')

def count_dinucleotides(input_f: str) -> dict: 
    try:
        input_length = len(input_f)
        for i in range(input_length -1):
            count[input_f[i] + input_f[i + 1]] += 1
        return count
    except Exception:
        raise Exception('Exception while counting dinucleotides')
            
def generate_and_write_htlm(input_f: str, file_name: str) -> None: 
    generate_dinucleodites()
    count_dinucleotides(input_f)
    write_file(file_name, "<div style='width: 100px; border: 1px solid #111; height: 100px; float: left; color: #fff; background-color: rgba(70, 3, 194, ")

if __name__ == '__main__':
    # set initial values 
    count = {}
    nucleotides = ['A', 'T', 'C', 'G']

    # human nucleotides
    file18s_human = read_file('18s_humano.fasta').replace('\n', '')
    generate_and_write_htlm(file18s_human, "18s_human.html")

    # bacterium nucleotides
    file16s_bacterium = read_file('16s_bacteria.fasta').replace('\n', '')
    generate_and_write_htlm(file16s_bacterium, "16s_bacterium.html")
